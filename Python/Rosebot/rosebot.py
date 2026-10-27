from Python.Rosebot import rosebot_sensors
import gpiozero as gz
from rosebot_drive_system import DriveSystem

class Rosebot:
    def __init__(self):
        self.drive_system = DriveSystem()
        self.leds = None
        self.ultrasonic = rosebot_sensors.Ultrasonic()
        self.line_sensors = rosebot_sensors.LineSensor()
        self.buzzer = gz.Buzzer(17)
        self.adc = None