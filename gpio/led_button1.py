# GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=192.168.4.158

from gpiozero import PWMLED, Button
from time import sleep
from signal import pause
from gpiozero.pins.pigpio import PiGPIOFactory

pi_host = '192.168.4.158'
factory = PiGPIOFactory(host=pi_host)
green = PWMLED(17, pin_factory=factory)
button = Button(2, pin_factory=factory)

pwm_value = 0
pwm_type = 0

while True:
    if pwm_type == 0:
        if button.is_active:
            pwm_value += 0.1
        if pwm_value >= 0.9:
            pwm_type = 1
    elif pwm_type == 1:
        if button.is_active:
            pwm_value -= 0.1
        if pwm_value <= 0.1:
            pwm_type = 0
    print(pwm_value)
    green.value = pwm_value
