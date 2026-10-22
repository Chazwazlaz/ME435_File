import motor
import time

class DriveSystem:

    def __init__(self):
        self.motor = motor.OrdinaryCar()

    def scale_speed(self, speed):
        """ scales a speed from -100 to 100 to a duty cycle from -4095 to 4095 """
        return int(speed / 100 * 4095)

    def set_speeds(self, left_front, left_rear, right_front, right_rear):
        """ pass in 4 speeds each -100 to 100 to set the 4 wheels of the robot """
        self.motor.set_motor_model(self.scale_speed(left_front), self.scale_speed(left_rear), self.scale_speed(right_front), self.scale_speed(right_rear))

    def go(self, left_wheel_speed, right_wheel_speed):
        """speeds as integers from -100 to 100"""
        self.set_speeds(left_wheel_speed, left_wheel_speed, right_wheel_speed, right_wheel_speed)

        pass

    def stop(self):
        self.set_speeds(0, 0, 0, 0)
        pass

    def go_straight_for_seconds(self, seconds, speed):
        """go straight for a given number of seconds at a given speed"""
        self.go(speed, speed)
        time.sleep(seconds)
        self.stop()
        pass

    def go_straight_for_inches(self, inches, speed):
        """go straight for a given number of inches at a given speed"""
        m = 0.2
        B = 0
        seconds = inches / (m * speed * B)
        self.go_straight_for_seconds(seconds, speed)    
