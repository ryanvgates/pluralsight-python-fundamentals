import unittest
import quickmaths


class QuickMathsTest(unittest.TestCase):
    def test_add(self):
        result = quickmaths.add(1,3)
        self.assertEqual(result, 4)
