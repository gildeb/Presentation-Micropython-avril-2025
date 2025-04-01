#
#  Faire clignoter une led
#
from machine import Pin
from time import sleep_ms

led = Pin(1, Pin.OUT)  #  led entre pin 1 et GND

for k in range(10):
    led.on()     # équivalent à led.value(1)
    sleep_ms(500)
    led.off()    # équivalent à led.value(0)
    sleep_ms(500)

led.off()