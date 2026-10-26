import gpiozero as gz
import time
import signal

# LEDs (same wiring as in class)
red_led = gz.LED(14)
yellow_led = gz.LED(15)
green_led = gz.LED(18)

# Pattern buttons (new for this homework)
button_red = gz.Button(22, bounce_time=0.05)
button_yellow = gz.Button(23, bounce_time=0.05)
button_green = gz.Button(24, bounce_time=0.05)


button_play = gz.Button(25, bounce_time=0.05)

pattern = []


def record_press(led):
    led.on()
    pattern.append(led)
    print("Pattern length:", len(pattern))
    time.sleep(0.5)


def play_pattern():

    print("Playing", len(pattern), "flashes")
    for i, led in enumerate(pattern):
        led.on()
        time.sleep(0.5)
        led.off()
        if i < len(pattern) - 1:
            time.sleep(0.1)

    pattern.clear()
    print("Pattern cleared, ready for a new round")


def main():
    print("Sequence Repeater (Reverse Simon)")

    button_red.when_pressed = lambda: record_press(red_led)
    button_red.when_released = lambda: red_led.off()

    button_yellow.when_pressed = lambda: record_press(yellow_led)
    button_yellow.when_released = lambda: yellow_led.off()

    button_green.when_pressed = lambda: record_press(green_led)
    button_green.when_released = lambda: green_led.off()

    button_play.when_pressed = lambda: play_pattern()

    signal.pause()  


main()