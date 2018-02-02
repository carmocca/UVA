import unittest
import os
from main import *

dir = os.path.dirname(os.path.abspath(__file__))


class Tests(unittest.TestCase):
    def test_solve(self):
        candidates = ['John Doe', 'Jane Smith', 'Jane Austen']
        ballots = [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 2, 3], [3, 1, 2]]
        self.assertEqual(solve(candidates, ballots), ['John Doe'])

    def test_1(self):
        with open(dir + '/samples/input1.txt', 'r') as input_file, \
             open(dir + '/samples/output1.txt', 'r') as output_file:
            self.assertEqual(main(input_file), output_file.readlines())

    def test_2(self):
        with open(dir + '/samples/input2.txt', 'r') as input_file, \
             open(dir + '/samples/output2.txt', 'r') as output_file:
            self.assertEqual(main(input_file), output_file.readlines())

    def test_3(self):
        with open(dir + '/samples/input3.txt', 'r') as input_file, \
             open(dir + '/samples/output3.txt', 'r') as output_file:
            self.assertEqual(main(input_file), output_file.readlines())


if __name__ == '__main__':
    unittest.main()