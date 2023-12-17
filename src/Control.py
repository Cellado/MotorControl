import keyboard
from time import sleep 
Gp = True 
try:
    import RPi.GPIO as GPIO
except:
    print("Did not import GPIO")
    GP = False 

def on_key_event(event):
    print (f"you pressed {event}")

    if event.name == 'up up':
        print ('true')

keyboard.on_release(on_key_event)
    
keyboard.wait('esc up')
