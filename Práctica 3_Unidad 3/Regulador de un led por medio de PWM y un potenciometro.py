from machine import Pin,PWM,ADC
from time import sleep

led = PWM(Pin(15))
led.freq(1000) #Frecuencia de señal analogica

pot = ADC(Pin(27))

while True:
    led.duty(pot.read() // 4) #Regular la itencidad
    sleep(0.05)  