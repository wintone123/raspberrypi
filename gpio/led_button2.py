# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import LED, Button
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
green = LED(17, pin_factory=factory)
button = Button(2, pin_factory=factory)

button.when_activated = green.on
button.when_deactivated = green.off

pause()