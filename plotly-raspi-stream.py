import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
import serial

username = ''
api_key = ''
stream_token = ''

py.sign_in(username, api_key)

trace1 = Scatter(
    x=[],
    y=[],
    stream=dict(
        token=stream_token,
        maxpoints=200
    )
)

layout = Layout(
    title='Raspberry Pi Knee Flex Data'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

# Arduino reading on /dev/ttyACM0
serialPort = '/dev/ttyACM0'
ser = serial.Serial(serialPort, 9600, timeout=1)
print ser.readline()
value  = 0


i = 0
stream = py.Stream(stream_token)
stream.open()

#the main sensor reading loop
while True:
    sensor_data = ''

    sensor_data = ser.readline()
    stream.write({'x': i, 'y': sensor_data})
    i += 1
    # delay between stream posts
    time.sleep(0.25)
