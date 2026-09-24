import serial

print("Learning Pyserial")

ser = serial.Serial('COM5', 19200, timeout=10)

while not ser.is_open:
    print("Opening...")

ser.close()