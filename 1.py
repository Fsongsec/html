import time

class Elevator:
    def __init__(self):
        self.current_floor = 1
        self.destinations = set()
        self.door_open = False

    def add_destination(self, floor):
        self.destinations.add(floor)

    def remove_destination(self, floor):
        if floor in self.destinations:
            self.destinations.remove(floor)

    def move(self):
        while self.destinations:
            next_floor = min(self.destinations) if self.current_floor < min(self.destinations) else max(self.destinations)
            if next_floor > self.current_floor:
                self.current_floor += 1
            elif next_floor < self.current_floor:
                self.current_floor -= 1
            self.arrive()
            time.sleep(2)  # 2秒延迟

    def arrive(self):
        print(f"Elevator arrived at floor {self.current_floor}")
        self.remove_destination(self.current_floor)
        if self.current_floor in self.destinations:
            self.open_door()

    def open_door(self):
        if not self.door_open:
            print("Opening door...")
            time.sleep(3)  # 开门3秒
            self.door_open = True

    def close_door(self):
        if self.door_open:
            print("Closing door...")
            time.sleep(3)  # 关门3秒
            self.door_open = False

    def display_panel(self):
        for floor in range(1, 13):
            if floor == self.current_floor:
                print("1", end="\t")
            else:
                print(floor, end="\t")
            if floor % 4 == 0:
                print()
        print("关闭                   打开")


elevator = Elevator()
elevator.display_panel()

while True:
    command = input("请输入目标楼层或其他需求：")
    if command.isdigit():
        floor = int(command)
        if 1 <= floor <= 12:
            elevator.add_destination(floor)
            elevator.move()
        elif command == "0":
            print("当前楼层：", elevator.current_floor)
            elevator.close_door()
        elif command == "00":
            print("当前楼层：", elevator.current_floor)
            elevator.open_door()
        else:
            print("无效的命令，请重新输入！")
