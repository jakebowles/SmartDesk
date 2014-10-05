void setup()
{
    // initialize serial communications
    Serial.begin(9600); 
}

void loop()
{
    int sensor;
    int angle;

    
    // read the voltage from the voltage divider (sensor plus resistor)
    sensor = analogRead(0);

    // convert the voltage reading to inches
    // the first two numbers are the sensor values for straight (768) and bent (853)
    // the second two numbers are the degree readings we'll map that to (0 to 90 degrees)
    angle = map(sensor, 510, 400, 0, 90);
    // note that the above numbers are ideal, your sensor's values will vary
    // to improve the accuracy, run the program, note your sensor's analog values
    // when it's straight and bent, and insert those values into the above function.

    // print out the result
//    Serial.print("analog input: ");
//    Serial.print(sensor,DEC);
//    Serial.print(" degrees: ");
//    Serial.println(degrees,DEC);
      //Serial.println(degrees, DEC);
      String angleString = String(angle);
      Serial.println(angleString);
    delay(10);// pause before taking the next reading
    
}
