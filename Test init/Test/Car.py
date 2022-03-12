class Car(object):
    def __init__(self):
        self.Wheels = 4
        self.Coolor = "Green"

    def print(self):
        return (self.Wheels, self.Coolor)

if __name__ == "__main__":
    car = Car()
    print(car.print())


