import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print((self.x, self.y))

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, x2, y2):
        distance = math.sqrt((self.x - x2) ** 2 + (self.y - y2) ** 2)
        print(distance)

p1 = Point(1, 3)
p1.show() 

p1.move(4, 7)
p1.show() 

p1.dist(10, 10)