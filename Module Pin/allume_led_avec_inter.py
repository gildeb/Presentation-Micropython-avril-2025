#
#  Allumer une led onboard en connectant
#  la pin 3 au 3.3V
#
from machine import Pin
from time import sleep

led = Pin(1, Pin.OUT)      # led entre pin 1 et GND
p3 = Pin(3, Pin.IN)        # interrupteur
p3.init(pull=Pin.PULL_DOWN)

while True:
    led.value(p3.value())
    sleep(0.1)