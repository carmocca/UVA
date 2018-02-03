import unittest
import os
from main import *

dir = os.path.dirname(os.path.abspath(__file__))


class Tests(unittest.TestCase):

    def test_1(self):
        with open(dir + '/samples/input.txt', 'r') as input_file, \
             open(dir + '/samples/output.txt', 'r') as output_file:
            self.assertEqual(main(input_file), output_file.readlines())


if __name__ == '__main__':
    unittest.main()