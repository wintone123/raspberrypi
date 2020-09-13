# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
button = Button(16, pin_factory=factory)

a = 0
button_type = 0

while True:
    if button.is_pressed:
        a += 1
        print(a)
    