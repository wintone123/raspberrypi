# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import PWMLED, Button
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory
from random import randint

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)

led_red = PWMLED(22, pin_factory=factory)
led_green = PWMLED(27, pin_factory=factory)
led_blue = PWMLED(17, pin_factory=factory)

button_red = Button(16, pin_factory=factory)
button_green = Button(20, pin_factory=factory)
button_blue = Button(21, pin_factory=factory)

led_red.value = 0
led_green = 0
led_blue.value = 0

