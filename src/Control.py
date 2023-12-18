import keyboard
import time
Gp = True 
try:
    import RPi.GPIO as GPIO
except:
    print("Did not import GPIO")
    Gp = False 
# Motor 1
Motor1F = 11
Motor1B = 13

# Motor 2
Motor2F = 29 
Motor2B = 31

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
        
    



