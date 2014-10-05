import plotly.plotly as py
from plotly.graph_objs import Scatter, Layout, Figure
import time
# import readadc
import serial

username = 'jakebowles'
api_key = 'ocibgkma3y'
stream_token = 'tlkcizcewu'

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
    title='Raspberry Pi Need Flex Data'
)

fig = Figure(data=[trace1], layout=layout)

print py.plot(fig, filename='Raspberry Pi Streaming Example Values')

# Arduino reading COM3
serialPort = '/dev/ttyACM0'
ser = serial.Serial(serialPort, 9600, timeout=1)
print ser.readline()
value  = 0

# temperature sensor connected channel 0 of mcp3008
# sensor_pin = 0
# readadc.initialize()

i = 0
stream = py.Stream(stream_token)
stream.open()

#the main sensor reading loop
while True:
        #sensor_data = readadc.readadc(sensor_pin, readadc.PINS.SPICLK, readadc.PINS.SPIMOSI, readadc.PINS.SPIMISO, readadc.PINS.SPICS)
        sensor_data = ''

	sensor_data = ser.readline()
	stream.write({'x': i, 'y': sensor_data})
        i += 1
        # delay between stream posts
        time.sleep(0.25)
