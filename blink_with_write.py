import time
import sys
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

pin1=11
pin2=12
iter=int(input(f"Number of blinks"))

DEBUG= False
  if "-debug" in sys.argv:
    DEBUG = True

LED_IS_ON = False

GPIO.setup(pin1, GPIO.IN)
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2, GPIO.LOW)

with open('data.txt', 'w') as data:
  while iter>0:
    iter -= 1
    input = GPIO.input(pin1)
    if input==True:
      GPIO.output(pin2, GPIO.HIGH)
      data.write(f'{time.time():1.0f} {input}\n')
      sleep(1)
      if DEBUG:
         print(f'LED is on: {LED_IS_ON}')
      LED_IS_ON = not(LED_IS_ON)
      GPIO.output(pin2, GPIO.LOW)
      sleep(1)
    else:
      GPIO.output(pin2, GPIO.LOW)
GPIO.cleanup()

