from Shape import Shape
class Rectangle:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width
    def area(self):
        print(self.lenght*self.width)
rectangle = Rectangle(10,20)
rectangle.area()