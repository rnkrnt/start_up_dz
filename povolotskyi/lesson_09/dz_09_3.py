class Parallelogram:
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def get_area(self):
        return self.__width * self.__length

class Square(Parallelogram):
    def __init__(self, width):
        Parallelogram.__width = width

    def get_area(self):
        return self.__width * self.__width


parallel = Parallelogram(10, 20)
print(parallel.get_area())
square = Square(10)
print(square.get_area())