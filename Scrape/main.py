from webscrape import get_data
#from motor import MotorClockwise, MotorAntiClockwise, MotorLeft, MotorRight, MotorStop, BeltStop
import time

def main():
    main_loop()

directions_list = ['Up', 'Down', 'Left', 'Right']

def live_data():
    result = get_data()
    split = result.split(',')
    direction = split[0]
    id = split[1]
    return id, direction #return split[0], split[1]



def main_loop():
    old_id = live_data()[0]
    while True:
        time.sleep(0.1)
        new_id, direction = live_data()

        if old_id != new_id:
            old_id = new_id
            print(direction)
            if direction == directions_list[0]:
                #MotorClockwise()
                print("Forwards")
            elif direction == directions_list[1]:
                print("Back")
                #MotorAntiClockwise()
            elif direction == directions_list[2]:
                print("Left")
                #MotorLeft()
            elif direction == directions_list[3]:
                print("Right")
                #MotorRight()
        time.sleep(0.5)
        #MotorStop()

if __name__ == "__main__":
    main()


