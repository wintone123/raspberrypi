# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import LED, Button
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory
from random import randint

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
led_yellow = LED(17, pin_factory=factory)
led_blue = LED(27, pin_factory=factory)
led_green = LED(22, pin_factory=factory)
led_red = LED(5, pin_factory=factory)
button_yellow = Button(3, pin_factory=factory)
button_blue = Button(2, pin_factory=factory)

a = randint(1, 4)
sleep(a)
led_green.on()

while True:
    if button_yellow.is_pressed:
        led_green.off()
        led_yellow.on()
        print("yellow first!")
        break
    elif button_blue.is_pressed:
        led_green.off()
        led_blue.on()
        print("blue first!")
        break

led_red.on()

sleep(2)
led_red.off()
led_blue.off()
led_yellow.off()
led_green.off()





