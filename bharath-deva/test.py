import unittest
import dummy

class Test(unittest.TestCase):
    def test_positive(self):
        result = dummy.Sumofthenumber(123)
        self.assertEqual(result,6)
    
    def test_negative(self):
        result = dummy.Sumofthenumber("abc")
        self.assertEqual(isinstance(result,ValueError),True)

unittest.main()
