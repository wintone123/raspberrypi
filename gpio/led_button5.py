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
button_white = Button(26, pin_factory=factory)

red_value = 0
green_value = 0
blue_value = 0

led_red.value = 0
led_green.value = 0
led_blue.value = 0

led_red_type = 0
led_green_type = 0
led_blue_type = 0


while True:
    if button_red.is_pressed:
        if led_red_type == 0:
            red_value += 0.1
            if red_value >= 0.9:
                led_red_type = 1
        elif led_red_type == 1:
            red_value -= 0.1
            if red_value <= 0.1:
                led_red_type = 0
        print("red:", red_value)
        led_red.value = red_value
        sleep(0.3)

    if button_green.is_pressed:
        if led_green_type == 0:
            green_value += 0.1
            if green_value >= 0.9:
                led_green_type = 1
        elif led_green_type == 1:
            green_value -= 0.1
            if green_value <= 0.1:
                led_green_type = 0
        print("green:", green_value)
        led_green.value = green_value
        sleep(0.3)

    if button_blue.is_pressed:
        if led_blue_type == 0:
            blue_value += 0.1
            if blue_value >= 0.9:
                led_blue_type = 1
        elif led_blue_type == 1:
            blue_value -= 0.1
            if blue_value <= 0.1:
                led_blue_type = 0
        print("blue:", blue_value)
        led_blue.value = blue_value
        sleep(0.3)
    
    if button_white.is_pressed:
        break

led_red.value = 0
led_green.value = 0
led_blue.value = 0