import unittest

def func(z,y):
	return z + y

class MyTestClass(unittest.TestCase):
	
	def test_one(self):
		result = func(4,4)
		self.assertTrue(result == 8, "Shoud be 8")

	def test_2(self):
		ress = func(-1,2)
		self.assertTrue(ress == 1, "Expect 1")


if __main__ == "__main__"
	unittest.main()
