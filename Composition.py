class Room:
    pass
class House:
    def __init__(self):
        self.room = Room()
house = House()
print(house.room)