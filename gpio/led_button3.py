# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import LED, Button
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory
from random import randint

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
led_green = LED(17, pin_factory=factory)
button_yellow = Button(2, pin_factory=factory)
button_blue = Button(3, pin_factory=factory)

a = randint(2, 5)
sleep(a)
led_green.on()

while True:
    if button_yellow.is_pressed:
        print("yellow first!")
        break
    elif button_blue.is_pressed:
        print("blue first!")
        break

led_green.off()


