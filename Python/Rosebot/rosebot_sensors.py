import gpiozero as gz


class Ultrasonic:
    def __init__(self, port):
        self.sensor = gz.DistanceSensor(echo=22, trigger=27)

    def get_cm(self):
        """returns the distance in centimeters"""
        return self.sensor.distance * 100


class LineSensor:
    def __init__(self, port):
        pass

    def get_left(self):
        """returns the value of the left line sensor"""
        if self.left.value ==1:
            return "B"
        return "W"

    def get_right(self):
        """returns the value of the right line sensor"""
        if self.right.value ==1:
            return "B"
        return "W"

    def get_middle(self):
        """returns the value of the middle line sensor"""
        if self.middle.value ==1:
            return "B"
        return "W"

    def get_line_word(self):
        """returns a 3-bit word representing the line sensors"""
        return self.get_left() + self.get_middle() + self.get_right()
    


if __name__ == "__main__":
    print("quick dev testing of the Ultrasonic and LineSensor classes")
    robot = Rosebot()

    try:
        while True:
            # get the ultrasonic sensor reading
            distance = robot.ultrasonic.get_cm()
            print(f"Ultrasonic distance: {distance:.2f} cm")

            # get the line sensor readings
            line_word = robot.line_sensors.get_line_word()
            print(f"Line sensor word: {line_word}")

 