#
#  duty = 1.5 ms ->   0°
#         0.5 ms -> -90°
#○        2.5 ms ->  90°
#
from machine import PWM

servo = PWM(freq=50, duty_ns=1500000)

def angle(x):
    if (x < -90) or (x > 90):
        print('angle non valide')
        return
    duty = int((1.5 + x/90)*1000000)
    servo.duty_u16(duty)
