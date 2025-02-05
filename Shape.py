class Shape:
    def area (self):
        print(0)
class Square(Shape):
    def __init__ (self, lenght):
        self.lenght = lenght
    def area(self):
        print(self.lenght**2)

sh = Shape()
sh.area()
        
sh = Square(5)
sh.area()