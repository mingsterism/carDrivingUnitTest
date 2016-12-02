from unittest import TestCase, main 
import selfDrivingCar

class SelfDrivingCarTest(TestCase):
	def setUp(self):
		self.car = selfDrivingCar.SelfDrivingCar()

	def test_stop(self):
		self.car.speed = 5
		self.car.stop()
		self.assertEqual(0, self.car.speed)

	def test_accelerate(self):
		self.car.speed = 0
		self.car._accelerate()
		self.assertEqual(1, self.car.speed)

if __name__ == '__main__':
	main()