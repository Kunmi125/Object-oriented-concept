class Vehicle:
    def __init__(self, a, b, c): 
        self.wheels = a
        self.color = b
        self.people = c
    def get_color(self):
        print("The color of the vehicle is", self.color)
    def set_color(self, new_color):
        self.color = new_color




bike = Vehicle(2, "blue", 2)
print(bike.color)
bike.get_color()
bicycle = Vehicle(2, "green", 1)
print(bicycle.people)

colour = input("What colour do you want your vehicle to be? ")
bike.set_color(colour)
bike.get_color()