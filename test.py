from Vehicles import Car, Motorcycle, Vehicle
import unittest


class TestExample(unittest.TestCase):

    def test1(self):
        car = Car('Tesla', 'Rodster', 2022)
        self.assertIsInstance(car, Vehicle)

    def test2(self):
        car = Car('Tesla', 'Rodster', 2022)
        self.assertEqual(car.numWheels, 4)

    def test3(self):
        moto = Motorcycle('Kawasaki', 'Ninja', 2021)
        self.assertEqual(moto.numWheels, 2)

    def test4(self):
        car = Car('Tesla', 'Rodster', 2022)
        car.testDrive()
        self.assertEqual(car.speed, 60)

    def test5(self):
        moto = Motorcycle('Kawasaki', 'Ninja', 2021)
        moto.testDrive()
        self.assertEqual(moto.speed, 75)

    def test6(self):
        car = Car('Tesla', 'Rodster', 2022)
        car.testDrive()
        car.park()
        self.assertEqual(car.speed, 0)

    def test7(self):
        moto = Motorcycle('Kawasaki', 'Ninja', 2021)
        moto.testDrive()
        moto.park()
        self.assertEqual(moto.speed, 0)


if __name__ == '__main__':
    unittest.main()
