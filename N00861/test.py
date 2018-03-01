import unittest
import os
from main import main

dir = os.path.dirname(os.path.abspath(__file__))


class Tests(unittest.TestCase):
    def test_1(self):
        with open(dir + '/samples/input1.txt', 'r') as input_file, \
             open(dir + '/samples/output1.txt', 'r') as output_file:
            # Incrementally test the first 60 values since
            # calculating all is too time consuming
            for x in (int(x) for x in output_file.readlines()[:60]):
                self.assertEqual(next(main(input_file)), x)


if __name__ == '__main__':
    unittest.main()