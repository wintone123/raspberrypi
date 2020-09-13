# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
button = Button(2, pin_factory=factory)


def plus_one():
    a += 1


def say_hello():
    print("hello")

def say_bye():
    print("bye")

a = 0

while True:
    if button.is_pressed:
        a += 1
        print(a)