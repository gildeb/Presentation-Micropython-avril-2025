from machine import PWM
from time import sleep_ms

led  = PWM(1, freq=1000, duty_u16=1)   # led entre pin 1 et gnd

for k in range(16):
    duty = led.duty_u16()*2
    led.duty_u16(duty)
    sleep_ms(100)

led.duty_u16(0)