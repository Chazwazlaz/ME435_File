import gpiozero as gz
import time
import signal

def basic_on_off():
    print("Basic On / Off")
    green_led = gz.DigitalOutputDevice(18)
    green_led.bl

    time.sleep(3)


def main():
    print('Leds')
    fancy_leds()

def fancy_leds():
    print("Fancy Leds")
    red_led = gz.LED(14)
    yellow_led = gz.LED(15)
    green_led = gz.LED(18)
    while True:
        red_led.on()
        time.sleep(0.01)
        red_led.off()
        yellow_led.on()
        time.sleep(0.01)
        yellow_led.off()
        green_led.on()
        time.sleep(0.01)
        green_led.off()
        time.sleep(0.01)



 

main()