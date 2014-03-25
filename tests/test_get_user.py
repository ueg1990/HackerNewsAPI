import unittest
import sys
from hn import HN

class TestGetUser(unittest.TestCase):
	def setUp(self):
		# check py version
		#self.PY2 = sys.version_info[0] == 2
		self.hn = HN()

	def tearDown(self):
		pass

	def test_get_user(self):
		test_user = self.hn.get_user('karangoeluw')
		self.assertEqual(test_user.username, 'karangoeluw')

if __name__ == '__main__':
     unittest.main()