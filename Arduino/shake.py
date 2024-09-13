from machine import Pin
import time

# Define the pin for the vibration sensor
vibration_sensor = Pin(2, Pin.IN)

# Define the pin for the LED
led = Pin(13, Pin.OUT)

while True:
    # Read the value from the vibration sensor
    sensor_value = vibration_sensor.value()
    
    # If vibration is detected (sensor output is HIGH)
    if sensor_value == 1:
        # Turn on the LED
        led.on()
        # Print a message to the console
        print("Vibration detected!")
    else:
        # Turn off the LED
        led.off()
    
    # Small delay to debounce the sensor
    time.sleep(0.1)