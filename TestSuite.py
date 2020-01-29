import unittest
from HW01 import classify_triangle

class TestHomework(unittest.TestCase):
    def test_clasify_triangle(self):
        #For Equilateral
        self.assertEqual(classify_triangle(3,3,3), 'It is an equilateral triangle')

        #For Isoceles
        self.assertEqual(classify_triangle(2,2,3), "It is an isoceles triangle")

        #For scalene
        self.assertEqual(classify_triangle(1,2,3), "It is a scalene triangle")

        #For right
        self.assertEqual(classify_triangle(3,4,5), "It is a scalene right triangle")
        


if __name__ == '__main__':
    unittest.main()