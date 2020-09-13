from gpiozero import PWMLED
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
red = PWMLED(17, pin_factory=factory)

while True:
    red.value = 0
    sleep(1)
    red.value = 0.2
    sleep(1)
    red.value = 0.4
    sleep(1)
    red.value = 0.6
    sleep(1)
    red.value = 0.8
    sleep(1)
    red.value = 1
    sleep(1)
