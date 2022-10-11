import unittest

from main import _min
from main import _max
from main import _sum
from main import _mult

class TestNumberMethods(unittest.TestCase):
    def test_min(self):
        self.assertEqual(_min([3, 5, 8, 1, 4]), 1)
        self.assertEqual(_min([70]), 70)
        self.assertEqual(_min([1.1, 1.3]), 1.1)
        self.assertEqual(_min([-4, -7, 0]), -7)
        self.assertEqual(_min([0, 0, 0]), 0)

    def test_max(self):
        self.assertEqual(_max([3, 5, 8, 1, 4]), 8)
        self.assertEqual(_max([70]), 70)
        self.assertEqual(_max([1.1, 1.3]), 1.3)
        self.assertEqual(_max([-4, -7, 0]), 0)
        self.assertEqual(_max([0, 0, 0]), 0)

    def test_sum(self):
        self.assertEqual(_sum([3, 5, 8, 1, 4]), 21)
        self.assertEqual(_sum([70]), 70)
        self.assertAlmostEqual(_sum([1.1, 1.3]), 2.4)
        self.assertEqual(_sum([-4, -7, 0]), -11)
        self.assertEqual(_sum([0, 0, 0]), 0)

    def test_mult(self):
        self.assertEqual(_mult([3, 5, 8, 1, 4]), 480)
        self.assertEqual(_mult([70]), 70)
        self.assertAlmostEqual(_mult([1.1, 1.3]), 1.43)
        self.assertEqual(_mult([-4, -7, 0]), 0)
        self.assertEqual(_mult([0, 0, 0]), 0)

    def test_empty(self):
        data = []
        with open("data.txt", "r") as file:
            line = file.readline()
            for x in line.split():
                data.append(float(x))
        self.assertGreater(len(data), 0)


if __name__ == '__main__':
    unittest.main()
