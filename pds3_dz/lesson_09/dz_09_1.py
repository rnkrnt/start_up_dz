class Car:
    def __init__(self, brand, color, volume_engine):
        self.brand = brand
        self.color = color
        self.volume_engine = volume_engine

    def go_ahead(self):
        return print("Едем прямо")

    def go_back(self):
        return print("Едем назад")

class Sportcat(Car):
    def __init__(self, brand, color, volume_engine):
        Car.brand = brand
        Car.color = color
        Car.volume_engine = volume_engine

    def go_left(self):
        return print("Едем влево")

    def go_right(self):
        return print("Едем вправо")

reno = Car("Reno", "black", "1.8")
bmw = Sportcat("BMW", "white", "6.4")

reno.go_ahead()
reno.go_back()
print()
bmw.go_ahead()
bmw.go_back()
bmw.go_right()
bmw.go_left()