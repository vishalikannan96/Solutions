import unittest
import sys
import cal
class Cal_unit(unittest.TestCase):
    def test_string1(self):
        self.assertEqual(cal.Sin_cal(30),-0.9880316240928618)
    def test_string2(self):
        self.assertRaises(cal.Sin_cal(40), 0.745113160479)
if __name__=='__main__':
    unittest.main()