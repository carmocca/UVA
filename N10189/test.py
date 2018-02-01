import unittest
import os
from main import *

dir = os.path.dirname(__file__)

class Tests(unittest.TestCase):
	def text(self):
		with open(dir + '/input', 'r') as input_file, \
				open(dir + '/output', 'r') as output_file:
			self.assertEqual(main(input_file), output_file)

if __name__ == '__main__':
	unittest.main()