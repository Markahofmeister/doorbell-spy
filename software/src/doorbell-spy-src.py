# gpiozero = controls GPIO pins
# gpiozero.tones = necessary to generate a tone if using a passive buzzer
# picamera = initializes/controls pi's camera
# datetime = fetches current date/time for image stamp
# signal = provides pause() function for event-driven flow
# time = provides sleep() function for a short program hiatus
# telepo = library to interface python with Telegram through API requests

from gpiozero import Button, LED,  MotionSensor, Buzzer, TonalBuzzer
from gpiozero.tones import Tone
from picamera import PiCamera
from datetime import datetime
from signal import pause
from time import sleep
import telepot
import creds

# Initialize camera 
camera = PiCamera()
camera.resolution=(1280, 720)
camera.framerate = 30
camera.iso = 400 
 
# Initialize peripheral objects 
led = LED(2)
pushButton = Button(3)
pir = MotionSensor(4)
#toneBuzzer = TonalBuzzer(18)
passiveBuzzer = Buzzer(18)

# Initialize the telegram bot object
doorbellBot = telepot.Bot(creds.api_key)

# Posts image to the telegram chat through a bot API call
def postImage(timestamp):
    doorbellBot.sendPhoto('@DoorbellCamTest', \
                photo=open('/home/pi/Pictures/%s.jpg' % timestamp, 'rb'))

# takes image and saves it to directory with timestamp
# no parameters, no return
def captureImage():
    print('Capturing Image')
    
    #Record current time and date
    timestamp = datetime.now().isoformat()
    
    #Capture Image
    camera.start_preview()
    sleep(2)
    camera.capture('/home/pi/Pictures/%s.jpg' % timestamp)
    camera.stop_preview()
    
    #Post image to telegram through function call to API request
    print('Posting Image to telegram')
    postImage(timestamp)

# blinks LED for 2 seconds, buzzer sounds for 2 seconds.
# no parameters, no return
def blinkAndBuzz():
    led.blink(3,1,1)
    passiveBuzzer.beep(1,1,1)
    captureImage()
    #toneBuzzer.play(Tone(800))
    #sleep(2)
    #toneBuzzer.stop()


try:
    # Just capture an image when motion is detected
    pir.when_motion = captureImage
    
    # If the button is pressed, capture an image,
    # but also blink the LED and sound the buzzer. 
    pushButton.when_pressed = blinkAndBuzz
    
    pause()
finally:
    pass