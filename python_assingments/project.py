class Elevator:

    def __init__(self):
        self.current_floor  = 1
        self.total_floor = 6

    def move_up(self):
        self.current_floor+= 1
        if self.current_floor > self.total_floor:
            self.current_floor == 6
        print(self.current_floor)

    def move_down(self):
        self.current_floor-= 1
        if self.current_floor < 1:
            self.current_floor == 1
        print(self.current_floor)

    
    def elevator_helper(self):
        engine.say("Enter your current floor")
        engine.runAndWait()
        curr_floor = int(input('Enter your current floor: '))
        lift_position = elevator.current_floor

        if lift_position == curr_floor:
            print('Lift is on the same floor.')
            engine.say("Lift is on the same floor")
            engine.runAndWait()
            
            print('Opening the doors now.')
            engine.say("Opening the doors now")
            engine.runAndWait()
            
            
            engine.say("Enter the destination floor")
            engine.runAndWait()
            dest_floor = int(input('Enter the destination floor: '))
            
        else:
            print('Lift is on the {} floor.'.format(elevator.current_floor))
            if curr_floor < elevator.current_floor:
                print('Lift is coming DOWN.')
                engine.say("Lift is coming DOWN")
                engine.runAndWait()
                
            else:
                print('Lift is coming UP.')
                engine.say("Lift is coming UP")
                engine.runAndWait()
                
            
            engine.say("Enter the destination floor")
            engine.runAndWait()
            dest_floor = int(input('Enter the destination floor: '))
            
        elevator.current_floor = curr_floor

        print('Door are closing.')
        engine.say("Door are closing")
        engine.runAndWait()
        
        elevator.current_floor = curr_floor
        return dest_floor, curr_floor


    def call_lift(self, direction, dest_floor, in_floor):
        while self.current_floor != dest_floor and (self.current_floor in range(1, self.total_floor)):
            if direction == 'up':
                self.move_up()
                time.sleep(1)
            elif direction == 'down':
                self.move_down()
                time.sleep(1)
        self.current_floor = dest_floor
        print("Reached Destination")
        engine.say("Reached Destination")
        engine.runAndWait()

        print('Opening Door Now.')
        engine.say("OPENING DOOR NOW")
        engine.runAndWait()
    



if __name__== '__main__':

    import pyttsx3, time


    engine = pyttsx3.init()
    

    #instance of an Elevator
    elevator = Elevator()
    
    while True:

        #When elevator is on the first floor
        if elevator.current_floor == 1:
            user_call = input("Enter U to go UP: ")
        #When elevator is on the Top floor
        elif elevator.current_floor == 5:
            user_call = input("Enter D to go DOWN: ")
        else:
            user_call = input("Enter U to go UP or D to go DOWN:")

        if user_call.upper() == 'U':

            dest_floor, curr_floor = elevator.elevator_helper()
            
            print('Going UP.')
            engine.say("Going UP")
            engine.runAndWait()
            
            elevator.call_lift('up',dest_floor, curr_floor)
        elif user_call.upper() == 'D':

            dest_floor, curr_floor = elevator.elevator_helper()
            
            print('Going DOWN.')
            engine.say("Going Down")
            engine.runAndWait()
            
            elevator.call_lift('down',dest_floor, curr_floor)





            






