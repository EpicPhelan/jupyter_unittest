import unittest
from program import find_max

class Test_Program(unittest.TestCase):
    #class for test

    #methods are the tests
    def test_case_1(self):
        test_list = [1,2,3]
        self.assertEqual(find_max(test_list), 3)

    def test_case_2(self):
        test_list = [1,2,3,4,5,6,7,8,9,10]
        self.assertEqual(find_max(test_list), 10)


if __name__ == '__main__':
    unittest.main(verbosity=2)