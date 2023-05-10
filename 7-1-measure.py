import matplotlib.pyplot as plt
import RPi.GPIO as GPIO
import time


def decimal2binary(value):
    return [int(i) for i in bin(value)[2:].zfill(8)]


def adc():
    level = 0
    for i in range(bits - 1, -1, -1):
        level += 2**i
        GPIO.output(dac, decimal2binary(level))
        time.sleep(0.01)
        comp_val = GPIO.input(comp)
        if (comp_val == 0):
            level -= 2**i
    return level



def num2_dac_leds(value):
    signal = decimal2binary(value)
    GPIO.output(dac, signal)
    return signal


# -------- constants -----------
dac    = [26, 19, 13, 6, 5, 11, 9, 10]
leds   = [21, 20, 16, 12, 7, 8, 25, 24]
comp   = 4
troyka = 17
bits   = len(dac)
levels = 2 ** bits
max_voltage = 3.3
# ------------------------------


GPIO.setmode(GPIO.BCM)

GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(troyka, 0)


data_volts = []
data_times = []

try:
    start_time = time.time()

    val = 0
    while val < 133:
        val = adc()
        print(val, decimal2binary(val), " volts - {:.3}".format(val / levels * max_voltage))
        num2_dac_leds(val)
        data_volts.append(val)
        data_times.append(time.time() - start_time)
    
    GPIO.output(troyka, 1)

    while val > 42:
        val = adc()
        print(val, decimal2binary(val), " volts - {:.3}".format(val / levels * max_voltage))
        num2_dac_leds(val)
        data_volts.append(val)
        data_times.append(time.time() - start_time)

    end_time = time.time()

    with open("settings.txt", 'w') as f:
        f.write(str((end_time - start_time) / len(data_volts)))
        f.write("\n")   
        f.write(str(max_voltage / 256))
    
    print(end_time - start_time, " cecs\n", (end_time - start_time) / len(data_volts), "\n", len(data_volts) / (end_time - start_time), "\n", max_voltage / 256)


finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, GPIO.LOW)
    GPIO.cleanup()


data_volts_str = [str(item) for item in data_volts]
data_times_str = [str(item) for item in data_times]

with open("data_volts.txt", 'w') as f:
    f.write("\n".join(data_volts_str))

with open("data_times.txt", 'w') as f:
    f.write("\n".join(data_times_str))


plt.plot(data_times, data_volts)
plt.show()