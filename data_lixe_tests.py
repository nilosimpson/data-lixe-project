import unittest

class TestDataLixe(unittest.TestCase):

    def test_true(self):
        self.assertEqual(True, True, "Should be True")

    def test_false(self):
        self.assertEqual(False, False, "Should be True")

if __name__ == '__main__':
    unittest.main()
