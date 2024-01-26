import RPi.GPIO as GPIO
import time

# Set the GPIO pin for the light sensor
light_sensor_pin = 17

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(light_sensor_pin, GPIO.IN)

try:
    while True:
        # Read the value of the light sensor
        light_value = GPIO.input(light_sensor_pin)

        if light_value == 0:
            print("Light is detected")  # Change this message to suit your needs
        else:
            print("Darkness detected")  # Change this message to suit your needs

        # Delay before reading the sensor again
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    GPIO.cleanup()
