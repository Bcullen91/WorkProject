import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(2, GPIO.OUT)
GPIO.output(2, GPIO.HIGH)

try:
    GPIO.output(2, GPIO.LOW)
    print("One")
    time.sleep(3)
    GPIO.cleanup()
    print("Goodbye")
except KeyboardInterrupt:
    print("Quit")
    GPIO.cleanup()
    