import unittest
import os
from main import main

dir = os.path.dirname(os.path.abspath(__file__))


class Tests(unittest.TestCase):

    def test_1(self):
        with open(dir + '/samples/input1.txt', 'r') as input_file, \
             open(dir + '/samples/output1.txt', 'r') as output_file:
            self.assertEqual(len(main(input_file)), int(output_file.readline()))

    def test_2(self):
        with open(dir + '/samples/input2.txt', 'r') as input_file, \
             open(dir + '/samples/output2.txt', 'r') as output_file:
            self.assertEqual(len(main(input_file)), int(output_file.readline()))

    def test_3(self):
        with open(dir + '/samples/input3.txt', 'r') as input_file, \
             open(dir + '/samples/output3.txt', 'r') as output_file:
            self.assertEqual(len(main(input_file)), int(output_file.readline()))

    def test_4(self):
        with open(dir + '/samples/input4.txt', 'r') as input_file, \
             open(dir + '/samples/output4.txt', 'r') as output_file:
            self.assertEqual(len(main(input_file)), int(output_file.readline()))

    def test_5(self):
        with open(dir + '/samples/input5.txt', 'r') as input_file, \
             open(dir + '/samples/output5.txt', 'r') as output_file:
            self.assertEqual(len(main(input_file)), int(output_file.readline()))


if __name__ == '__main__':
    unittest.main()