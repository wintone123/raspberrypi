# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import LED
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
red = LED(17, pin_factory=factory)

red.blink()

pause()


