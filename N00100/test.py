import unittest
import os
from main import *

dir = os.path.dirname(os.path.abspath(__file__))


class Tests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(solve(1, 10), 20)

    def test_2(self):
        self.assertEqual(solve(100, 200), 125)

    def test_3(self):
        self.assertEqual(solve(201, 210), 89)

    def test_4(self):
        self.assertEqual(solve(900, 1000), 174)

    def test_5(self):
        with open(dir + '/samples/input1.txt', 'r') as input_file, \
             open(dir + '/samples/output1.txt', 'r') as output_file:
            self.assertEqual(main(input_file), output_file.readlines())

    def test_6(self):
        with open(dir + '/samples/input2.txt', 'r') as input_file, \
             open(dir + '/samples/output2.txt', 'r') as output_file:
            self.assertEqual(main(input_file), output_file.readlines())

    def test_7(self):
        with open(dir + '/samples/input3.txt', 'r') as input_file, \
             open(dir + '/samples/output3.txt', 'r') as output_file:
            self.assertEqual(main(input_file), output_file.readlines())


if __name__ == '__main__':
    unittest.main()
