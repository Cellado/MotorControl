import keyboard
from time import sleep 
Gp = True 
try:
    import RPi.GPIO as GPIO
except:
    print("Did not import GPIO")
    Gp = False 

def on_key_event(event):
    """
    Checks for keys being pressed and Prints the key being pressed. 

    Parameters: 
    event: The key being pressed. 

    """
    print (f" you pressed {event}")

    if event.name == "up":
        print ('true')

keyboard.on_release(on_key_event)
    
keyboard.wait('esc')

def motorInit():
    if Gp == True:
        print("working")
        GPIO.setmode(GPIO.BOARD)



