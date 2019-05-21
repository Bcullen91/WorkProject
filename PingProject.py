import time
import RPi.GPIO as GPIO


# Suppress warnings
GPIO.setwarnings(False)

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BOARD)

# Set LED pin as output
GPIO.setup(12, GPIO.OUT)


GPIO.output(12, GPIO.HIGH) # Turn LED on
print("x")
time.sleep(1)                   # Delay for 1 second
GPIO.output(12, GPIO.LOW)  # Turn LED off
print("y")
time.sleep(1)                   # Delay for 1 second
GPIO.cleanup()
print("Finshed")