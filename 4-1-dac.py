import RPi.GPIO as GPIO

dac = [26, 19, 13, 6, 5, 11, 9, 10]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]


def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False

def is_float(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


try:
    while True:
      k = input()
      if(k == 'q'):
          break
      elif(is_int(k)):
          num = int(k)
          if(0<=num<=255):
           GPIO.output(dac, decimal2binary(num)) 
           voltage = (num/2**8) * 3.3
           print("Напряжение на выходе равно: ", voltage)
          else:
              if(num < 0):
                      print("negative number")
              if(num > 255):
                      print("number too big for 8 bit representation") 
      elif(is_float(k)):
              print("non-integer number")
      else:
              print("not a number")
        

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
