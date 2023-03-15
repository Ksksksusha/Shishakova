import RPi.GPIO as GPIO
import time as time


dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


try:
    str = input()
    period = float(str) / 256
    while True:
        for k in range (0, 255):
            GPIO.output(dac, decimal2binary(k)) 
            time.sleep(period)
        for k in range (0, 255):
            GPIO.output(dac, decimal2binary(255-k)) 
            time.sleep(period)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
