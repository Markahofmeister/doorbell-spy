# gpiozero = controls GPIO pins
# picamera = initializes/controls pi's camera
# datetime = fetches current date/time for image stamp

from gpiozero import Button, LED,  MotionSensor, Buzzer
from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep
 
# Initialize peripheral objects 
camera = PiCamera()
pushButton = Button(2)
pir = MotionSensor(3)
led = LED(4)
buzzer = Buzzer(17)

# takes image and saves it to directory with timestamp
# no parameters, no return
def captureImage():
    timestamp = datetime.now().isoformat()
    camera.capture('/home/pi/%s.jpg' % timestamp)

# blinks LED for 2 seconds, buzzer sounds for 2 seconds.
# no parameters, no return
def blinkAndBuzz():
    captureImage
    led.blink(2,1,0,0,1,True)
    buzzer.beep(2,1,1,True)
try: 
    pir.when_motion = captureImage
    button.when_pressed = blinkAndBuzz
    
    pause()
finally:
    pass