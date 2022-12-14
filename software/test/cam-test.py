# gpiozero = controls GPIO pins
# picamera = initializes/controls pi's camera
# datetime = fetches current date/time for image stamp

from gpiozero import Button, LED
from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep
 
# Initialize camera 
camera = PiCamera()
camera.resolution=(1280, 720)
camera.framerate = 30
camera.iso = 400

# Initialize peripheral objects
button = Button(3)
led = LED(2)

# takes image and saves it to directory with timestamp
# no parameters, no return
def captureImage():
    timestamp = datetime.now().isoformat()
    # print(timestamp)
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Pictures/%s.jpg' % timestamp)
    camera.stop_preview()

# blinks LED for 2 seconds, buzzer sounds for 2 seconds.
# no parameters, no return
def blinkAndCap():
    captureImage()
    led.blink()
    
try: 
    button.when_pressed = blinkAndCap
    
    pause()
finally:
    pass
