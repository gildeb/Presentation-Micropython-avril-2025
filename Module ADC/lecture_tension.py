#
#  Lecture tension potentiomètre
#
from machine import ADC
from time import sleep_ms

a = ADC(0)   # point milieu potentiomètre -> pin 26

while True:
    tension = a.read_u16()*3.3/2**16
    print("u={:4.2f} V".format(tension))
    sleep_ms(300)
