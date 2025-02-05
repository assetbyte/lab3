class Print:
    def getString(self):
        return input()
    def printString(self, s):
        print(s.upper())

obj = Print()
s = obj.getString()
obj.printString(s)
