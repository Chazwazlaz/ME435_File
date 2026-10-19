import gpiozero as gz
import time
import signal

def button_state():
    button = gz.Button(25)

    while True:
        if button.is_pressed:
            print("Button Pressed")
        else:
            print("Button NOT Pressed")
        time.sleep(0.5)


def function_using_def():
    print("Function using def")

function_using_lambda = lambda: print("Function using lambda")


def button_events():
    print("Button Events")
    button = gz.Button(25)
    button.when_pressed = function_using_def
    button.when_released = function_using_lambda
    button.when_held = lambda: print("Button Held")


    signal.pause

def main():
    print('Pushbutton')
    button_events()

main()