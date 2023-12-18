import keyboard
import time
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


def on_key_event(event):
    """
    Checks for keys being pressed and Prints the key being pressed. 
    Parameters: 
    event: The key being pressed. 
    """
    print (f" you pressed {event}")
    if event.name == "up":
        print('up')
        try: 
            GPIO.output(Motor1F, GPIO.HIGH)
            GPIO.output(Motor1B, GPIO.LOW)
            GPIO.output(Motor2F, GPIO.HIGH)
            GPIO.output(Motor2B, GPIO.LOW)
            print("GPIO success")
        except:
            print("Tried GPIO up")
    if event.name == "down":
        print('down')
        try: 
            GPIO.output(Motor1B, GPIO.HIGH)
            GPIO.output(Motor1F, GPIO.LOW)
            GPIO.output(Motor2B, GPIO.HIGH)
            GPIO.output(Motor2F, GPIO.LOW)
        except:
            print("Tried GPIO down")

    if event.name == "space":
        print('space')
        try: 
            GPIO.output(Motor1F, GPIO.LOW)
            GPIO.output(Motor1B, GPIO.LOW)
            GPIO.output(Motor2F, GPIO.LOW)
            GPIO.output(Motor2B, GPIO.LOW)
        except:
            print("Tried GPIO space")

keyboard.on_release(on_key_event)  
keyboard.wait('esc')

try: 
    GPIO.cleanup()
except: 
    print("GPIO Clean")
    



