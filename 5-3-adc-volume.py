import RPi.GPIO as GPIO
import time as time

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

def num2dac(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal

def adc1():
    for value in range(levels):
        num2dac(value)
        time.sleep(0.01)
        if GPIO.input(comp) == 0:
            return value



def adc2():
    k = 0
    for i in range(bits - 1, -1, -1):
        k += 2**i
        GPIO.output(dac, decimal2binary(k))
        time.sleep(0.001)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            k -= 2**i
    return k


dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21, 20, 16, 12, 7, 8, 25, 24]
comp = 4
troyka = 17 
bits   = len(dac)
levels = 2 ** bits
max_voltage = 3.3
                                                                                             

GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

try:
    while True:
        val = adc2()
        k = 0
        for i in range(bits):
            if (val > i / 8 * levels):
                k += 2 ** i
        GPIO.output(leds, decimal2binary(k))
        
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(leds, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()