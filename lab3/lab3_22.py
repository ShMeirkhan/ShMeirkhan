
class StringManipulator:
    def __init__(self):
        self.string = ""

    def getString(self):
        self.string = input("Введите строку: ")

    def printString(self):
        print(self.string.upper())

if __name__ == "__main__":
    manipulator = StringManipulator()
    manipulator.getString()
    manipulator.printString()
