# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
led_blue = LED(17, pin_factory=factory)
led_green = LED(27, pin_factory=factory)
led_red = LED(22, pin_factory=factory)

led_blue.on()
led_red.off()
led_green.off()
sleep(1)
led_blue.off()
led_red.on()
led_green.off()
sleep(1)
led_blue.off()
led_red.off()
led_green.on()
sleep(1)
led_blue.on()
led_red.on()
led_green.off()
sleep(1)
led_blue.on()
led_red.off()
led_green.on()
sleep(1)
led_blue.off()
led_red.on()
led_green.on()
sleep(1)
led_blue.on()
led_red.on()
led_green.on()
sleep(1)
led_blue.off()
led_red.off()
led_green.off()
sleep(1)