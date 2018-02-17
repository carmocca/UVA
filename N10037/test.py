import unittest
import os
from main import main

dir = os.path.dirname(os.path.abspath(__file__))


class Tests(unittest.TestCase):

    def test_1(self):
        with open(dir + '/samples/input1.txt', 'r') as input_file, \
             open(dir + '/samples/output1.txt', 'r') as output_file:
            sol = main(input_file)
            expected = output_file.readlines()
            self.assertEqual(self.totals(sol), self.totals(expected))

    def test_2(self):
        with open(dir + '/samples/input2.txt', 'r') as input_file, \
             open(dir + '/samples/output2.txt', 'r') as output_file:
            sol = main(input_file)
            expected = output_file.readlines()
            self.assertEqual(self.totals(sol), self.totals(expected))

    def test_3(self):
        with open(dir + '/samples/input3.txt', 'r') as input_file, \
             open(dir + '/samples/output3.txt', 'r') as output_file:
            sol = main(input_file)
            expected = output_file.readlines()
            self.assertEqual(self.totals(sol), self.totals(expected))

    def totals(self, sol):
        res = []
        previous = None
        for line in sol:
            if previous == None:
                res.append(line)
                previous = line
            if line == '\n':
                previous = None
        return res


if __name__ == '__main__':
    unittest.main()
