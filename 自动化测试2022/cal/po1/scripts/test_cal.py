import unittest
import time
from parameterized import parameterized
from cal.po1.base.get_driver import GetDriver
from cal.po1.page.page import PageCal

data = [(1,1,2),(55,45,100),(66,3,71)]

class TestCal(unittest.TestCase):
    #driver = None
    @classmethod
    def setUpClass(cls):
        cls.driver = GetDriver().get_driver()
        cls.cal = PageCal(cls.driver)

    @parameterized.expand(data)
    def test_cal(self,a,b,c):
        self.cal.page_cal(a,b)
        time.sleep(3)
        try:
            result = self.cal.page_get_sum()
            self.assertEqual(int(result),c)
        except AssertionError:
            self.cal.page_get_image()
    @classmethod
    def tearDownClass(cls):
        GetDriver.quit_driver()