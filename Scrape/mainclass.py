from webscrapeclass import DataSalvage
#from motorclass import MotorActivation
import time

def main():
    peterporker = Activate("https://peterporker.pythonanywhere.com", True)
    peterporker.main_loop()


class Activate:
    directions_list = ['Up', 'Down', 'Left', 'Right']

    def __init__(self, website, headless):
        self.website = website
        self.headless = headless
        self.site = DataSalvage(website, headless)
        #self.motors = MotorActivation()

    def live_data(self):
        self.result = self.site.get_data()
        self.split = self.result.split(',')
        self.direction = self.split[0]
        self.id = self.split[1]
        return self.id, self.direction #return self.split[0], self.split[1]



    def main_loop(self):
        self.old_id = self.live_data()[0]
        try:
            while True:
                time.sleep(0.1)
                self.new_id, self.direction = self.live_data()

                if self.old_id != self.new_id:
                    self.old_id = self.new_id
                    print(self.direction)
                    if self.direction == self.directions_list[0]:
                        #self.motors.motor_clockwise()
                        print("Up")
                    elif self.direction == self.directions_list[1]:
                        print("Down")
                        #self.motors.motor_anti_clockwise()
                    elif self.direction == self.directions_list[2]:
                        print("Left")
                        #self.motors.motor_left()
                    elif self.direction == self.directions_list[3]:
                        print("Right")
                        #self.motors.motor_right()
                time.sleep(0.5)
                #self.motors.motor_stop()

        except KeyboardInterrupt:
            #self.motors.release_gpios()
            print("Keyboard Interrupt!!")


if __name__ == "__main__":
    main()


