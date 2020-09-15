# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import LEDBoard
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)

leds = LEDBoard(6, 5, 22, 27, 17, pin_factory=factory, pwm=True)

led_value = (0.1, 0.3, 0.5, 0.7, 0.9)

leds.value = led_value

sleep(1)

leds.off()