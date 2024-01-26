import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin1=11
pin2=12

GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2, GPIO.LOW)

while True:
  input = GPIO.input(pin1)
  if input==True:
    GPIO.output(pin2, GPIO.HIGH)
  else:
    GPIO.output(pin2, GPIO.LOW)
GPIO.cleanup()
