from time import time

from rosebot import Rosebot

def main():
    print("Lab 5a: Line Following")
    robot = rb.Rosebot()

    try:
        while True:
            # get the ultrasonic sensor reading
            
            # if distance < 20 cm stop the robot
            time.sleep(0.1)  # Small delay to avoid overwhelming the user with messages


    except KeyboardInterrupt:
        # Handle Crtl-C gracefully: stop the robot and close the camera window.
        robot.drive_system.stop()
        print("Exiting Lab 5a: Line Following")

