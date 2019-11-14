import unittest
from src.cal_sin import cal
class Cal_unit(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(cal.sin_cal('30'),-0.9880316240928618)
    def test_case2(self):
        self.assertEqual(cal.sin_cal('uyh'),'It is not number')
    def test_case3(self):
        self.assertEqual(cal.sin_cal('-30'),0.9880316240928618)
if __name__== '__main__':
    unittest.main()