import RPi.GPIO as GPIO
import time as time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

def adc():
    k = 0
    for i in range(bits - 1, -1, -1):
        k += 2**i
        GPIO.output(dac, decimal2binary(k))
        time.sleep(0.01)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            k -= 2**i
    return k


dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
troyka = 17 
bits   = len(dac)
levels = 2 ** bits
max_voltage = 3.3


GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        val = adc()
        print(val, decimal2binary(val), " volts - {:.3}".format(val / levels * max_voltage))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()
