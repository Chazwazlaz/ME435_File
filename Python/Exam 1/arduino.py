import serial
import time



class arduino:
    def __init__(self, port="/dev/ttyAMA10"):
        self.port = port

    def connect(self):
        self.ser = serial.Serial(self.port, baudrate=9600, timeout=15)
        time.sleep(2)
        self.ser.reset_input_buffer()

    def disconnect(self):
        if self.ser and self.ser.is_open:
            self.ser.close()
        

    def send_command(self, command):
        self.ser.reset_input_buffer()
        message_bytes = (command + "\n").encode()
        print(message_bytes)

        self.ser.write(message_bytes)

        response_bytes = self.ser.readline()
        print(response_bytes)
        response = response_bytes.decode().strip()
        return response


if __name__ == "__main__":
    print("LED Testing")
    LEDFlasher = arduino()
    LEDFlasher.connect()
    response = LEDFlasher.send_command("LED ON")
    print("Response: ", response)
    LEDFlasher.disconnect()
