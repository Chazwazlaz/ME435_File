import serial
import time



class PlateLoader:
    def __init__(self, port="/dev/ttyUSB0"):
        self.port = port

    def connect(self):
        self.ser = serial.Serial(self.port, baudrate=19200, timeout=15)
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
    print("Quick Plateloader testing")
    loader = PlateLoader()
    loader.connect()
    response = loader.send_command("RESET")
    print("Response: ", response)
    loader.disconnect()
