import unittest
import os
from main import main

dir = os.path.dirname(os.path.abspath(__file__))


class Tests(unittest.TestCase):
    def test_1(self):
        with open(dir + '/samples/input1.txt', 'r') as input_file, \
             open(dir + '/samples/output1.txt', 'r') as output_file:
            return self.check_valid_sol(input_file, output_file)

    def test_2(self):
        with open(dir + '/samples/input2.txt', 'r') as input_file, \
             open(dir + '/samples/output2.txt', 'r') as output_file:
            return self.check_valid_sol(input_file, output_file)

    def check_valid_sol(self, input, output):
        for valid, sol in main(input):
            theirs = int(output.readline())
            self.assertEqual(valid, theirs)
            if valid:
                # The solution might be different. Skip it
                for _ in range(len(sol)):
                    output.readline()


if __name__ == '__main__':
    unittest.main()
