# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import LEDBoard, ButtonBoard
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory
from random import randint, random
import numpy

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
leds_green = LEDBoard(27, 22, 5, 6, 13, 19, 26, pwm=True, pin_factory=factory)

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

for i in range(len(leds_green) + 2):
    if i <= 1:
        smooth_start(leds_green[i], value_up)
    elif i >= len(leds_green):
        smooth_end(leds_green[i - 2], value_up)
    else: 
        smooth_middle(leds_green[i - 2], leds_green[i], value_up)

leds_green.off()