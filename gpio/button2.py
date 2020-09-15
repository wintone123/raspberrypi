# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import Button
from gpiozero.pins.pigpio import PiGPIOFactory
from signal import pause
from time import sleep

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
red_button = Button(16, pin_factory=factory)


def plus_one(a):
    a += 1


def say_hello():
    print("hello")

def say_bye():
    print("bye")

a = 0

while True:
    if red_button.value == 1:
        a += 1
        print(a)
        sleep(1)