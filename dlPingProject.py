import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.out)
GPIO.setwarnings(False)
GPIO.cleanup()