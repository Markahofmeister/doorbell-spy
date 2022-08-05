# gpiozero = controls GPIO pins
# picamera = initializes/controls pi's camera
# datetime = fetches current date/time for image stamp
# signal = provides pause() function for event-driven flow
# time = provides sleep() function for a short program hiatus 

from gpiozero import Button, LED,  MotionSensor, Buzzer
from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep
import telepot

# Initialize camera 
camera = PiCamera()
camera.resolution=(1280, 720)
camera.framerate = 30
camera.iso = 400 
 
# Initialize peripheral objects 
led = LED(2)
pushButton = Button(3)
pir = MotionSensor(4)
buzzer = Buzzer(18)

# Initialize the telegram bot object
doorbellBot = telepot.Bot('5488078961:AAFaJivap_jWBhUzhWMHzKn7p_KTUw9bpF0')

# Posts image to the telegram chat through a bot API call
def postImage(timestamp):
    doorbellBot.sendPhoto('@DoorbellCamTest', \
                photo=open('/home/pi/Pictures/%s.jpg' % timestamp, 'rb'))

# takes image and saves it to directory with timestamp
# no parameters, no return
def captureImage():
    timestamp = datetime.now().isoformat()
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Pictures/%s.jpg' % timestamp)
    camera.stop_preview()
    postImage(timestamp)

# blinks LED for 2 seconds, buzzer sounds for 2 seconds.
# no parameters, no return
def blinkAndBuzz():
    captureImage()
    led.blink(2,1)
    buzzer.beep(2,1,1,True)


try:
    # Just capture an image when motion is detected
    pir.when_motion = captureImage
    
    # If the button is pressed, capture an image,
    # but also blink the LED and sound the buzzer. 
    pushButton.when_pressed = blinkAndBuzz
    
    pause()
finally:
    pass