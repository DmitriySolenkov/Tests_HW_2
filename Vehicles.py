class Vehicle():
    speed = 0

    def __init__(self, company, model, releaseYear):
        self.company = company
        self.model = model
        self.releaseYear = releaseYear

    def testDrive():
        pass

    def park():
        pass


class Car(Vehicle):
    numWheels = 4

    def testDrive(self):
        self.speed = 60

    def park(self):
        self.speed = 0


class Motorcycle(Vehicle):
    numWheels = 2

    def testDrive(self):
        self.speed = 75

    def park(self):
        self.speed = 0
