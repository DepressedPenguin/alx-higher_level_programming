#!/usr/bin/python3
# DP_PENGUIN
import unittest
def func(x,y):
	return x + y


class MyTestCase(unittest.TestCase):
	def test_1(self):
		res = func(2,4)
		self.assertEqual(res,6,"FAIL! RESULT SHOULD BE 6")

	def test_2(self):
		res = func(-1,2)
		self.assertEqual(res,2,"SHOULD Be 1")


if __name__ == "__main__":
    unittest.main()
