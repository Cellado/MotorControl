import time
import pynput
from pynput.keyboard import Key, Listener
from pynput.mouse import Listener as MouseListener


Gp = True 
try:
    import RPi.GPIO as GPIO
    print("imported GPIO")
except:
    print("Did not import GPIO")
    Gp = False 
# Motor 1
Motor1F = 11
Motor1B = 13

# Motor 2
Motor2F = 29 
Motor2B = 31

try: 
    GPIO.setmode(GPIO.BOARD)
    # Motor 1
    GPIO.setup(Motor1F, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    # Motor 2
    GPIO.setup(Motor2F, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
except:
    print("GPIO not available")


            #GPIO.output(Motor1F, GPIO.HIGH)
            #GPIO.output(Motor1B, GPIO.LOW)
            #GPIO.output(Motor2F, GPIO.HIGH)
            #GPIO.output(Motor2B, GPIO.LOW)

def on_press(key):
    print(f'{key} pressed')

def on_release(key):
    print(f'{key} released')

    if key == Key.esc:
        return False
        exit() 

def on_move(x, y):
    print(f'Mouse moved to ({x}, {y})')

with MouseListener(on_move=on_move) as listener:
    listener.join


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

try: 
    GPIO.cleanup()
except: 
    print("GPIO Clean")
    



