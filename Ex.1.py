class Elevator:
    def __init__(self, down_floor, up_floor):
        self.down_floor = down_floor
        self.up_floor = up_floor
        self.current_floor = down_floor
    def floor_up(self):
        if self.current_floor < self.up_floor:
            self.current_floor += 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the up floor.")
    def floor_down(self):
        if self.current_floor > self.down_floor:
            self.current_floor -= 1
            print(f"Elevator is now at floor {self.current_floor}")
        else:
            print("Elevator is already at the down floor.")
    def go_to_floor(self, target_floor):
        if target_floor > self.up_floor or target_floor < self.down_floor:
            print(f"Floor {target_floor} is out of range.")
            return
        print(f"Moving elevator to floor {target_floor}...")
        while self.current_floor < target_floor:
            self.floor_up()
        while self.current_floor > target_floor:
            self.floor_down()
# Testing the Elevator class
if __name__ == "__main__":
    elevator = Elevator(0, 10)
    elevator.go_to_floor(5)
    elevator.go_to_floor(0)