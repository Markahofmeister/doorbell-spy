from gpiozero import Button, LED
from signal import pause

led = LED(2)
button = Button(3)

button.when_pressed = led.blink

pause()