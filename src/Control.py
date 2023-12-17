import keyboard
try:
    import RPi.GPIO as GPIO
except:
    print("Did not import GPIO")
from time import sleep 
def on_key_event(event):
    print (f"you pressed {event}")

    if event.name == 'up':
        print ('true')
        
keyboard.on_release(on_key_event)
    
keyboard.wait('esc')
