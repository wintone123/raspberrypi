# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import PWMLED
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory
from random import random

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)

led_red = PWMLED(22, pin_factory=factory)
led_green = PWMLED(27, pin_factory=factory)
led_blue = PWMLED(17, pin_factory=factory)

i = 0
while i <= 5:
    led_red.value = random()
    led_green.value = random()
    led_blue.value = random()
    i += 1
    sleep(1)

led_red.value = 0
led_green.value = 0
led_blue.value = 0
