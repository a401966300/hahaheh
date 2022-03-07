import unittest
from cal.po1.page.page import PageCal

class TestCal(unittest.TestCase):

    def setUp(self):
        self.cal = PageCal()

    def test_cal(self):


    def tearDown(self):
        self.cal.driver.quit()