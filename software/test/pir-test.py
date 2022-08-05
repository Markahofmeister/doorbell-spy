from gpiozero import MotionSensor, LED
from signal import pause

led = LED(2)
pir = MotionSensor(4)

try:
    
    pir.when_motion = led.on
    pir.when_no_motion = led.off
    
    pause()
    
finally:
    pass