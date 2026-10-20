import plateloader

def main():
    print("Serial Menu")
    loader = plateloader.PlateLoader("/dev/ttyUSB0")
    loader.connect()
    print("0. Exit")
    print("1. RESET")
    print('2. X-AXIS"')
    print("3. Gripper")
    print("4. Z-AXIS")
    print("5. Status")

    while True:
        selection = int(input("Select an option: "))
        if selection == 0:
            break
        elif selection == 1:
            response = loader.send_command("RESET")
            print("Response: ", response)
        elif selection == 2:
            x_axis_choice = XAxisSubMenu()
            if x_axis_choice:
                response = loader.send_command("X-AXIS " + str(x_axis_choice))
                print("Response: ", response)
        elif selection == 3:
            gripper_choice = GripperSubMenu()

            if gripper_choice:
                if gripper_choice == 0:
                    response = loader.send_command("GRIPPER OPEN")
                elif gripper_choice == 1:
                    response = loader.send_command("GRIPPER CLOSE")
                print("Response: ", response)
        elif selection == 4:
            z_axis_choice = ZAxisSubMenu()
            if z_axis_choice:
                if z_axis_choice == 1:
                    response = loader.send_command("Z-AXIS EXTEND")
                elif z_axis_choice == 2:
                    response = loader.send_command("Z-AXIS RETRACT")
                print("Response: ", response)
        elif selection == 5:
            response = loader.send_command("STATUS")
            print("Response: ", response)
            


def XAxisSubMenu():
    print("X-Axis position selection: (1-5)")

    choice = int(input("Select an option: "))
    return choice

def GripperSubMenu():
    print("Gripper State:")
    print("0. Open")
    print("1. Close")
    choice = int(input("Select an option: "))
    return choice

def ZAxisSubMenu():
    print("Z-Axis State:")
    print("1. Extend")
    print("2. Retract")
    choice = int(input("Select an option: "))
    return choice

main()

