# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import RGBLED, Button
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory
from random import random

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
led = RGBLED(22, 27, 17, pin_factory=factory)
button_white = Button(26, pin_factory=factory)

while True:
    if button_white.is_pressed:
        break

    red_value = random()
    green_value = random()
    blue_value = random()
    led.color = (red_value, green_value, blue_value)

    sleep(0.5)

led.color = (0, 0, 0)