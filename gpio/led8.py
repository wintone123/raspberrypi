# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import LEDBoard, Button
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory
from random import randint, random
import numpy

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
leds_green = LEDBoard(27, 22, 5, 6, 13, 19, 26, 16, 20, 21, pwm=True, pin_factory=factory)
button_exit = Button(12, pin_factory=factory)

value_up = numpy.arange(0, 21) / 20

def smooth_start(led, value):
    for i in value:
        led.value = i

def smooth_middle(led1, led2, value):
    for i in value:
        led1.value = 1 - i
        led2.value = i

def smooth_end(led, value):
    for i in value:
        led.value = 1 - i

leds_green.off()

for i in range(len(leds_green) + 3):
    if i <= 2:
        smooth_start(leds_green[i], value_up)
    elif i >= len(leds_green):
        smooth_end(leds_green[i - 3], value_up)
    else: 
        smooth_middle(leds_green[i - 3], leds_green[i], value_up)

leds_green.off()