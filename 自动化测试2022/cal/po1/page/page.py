from selenium.webdriver.common.by import By
from cal.po1 import page
from cal.po1.base.base import CalBase


class PageCal(CalBase):

    def page_click_number(self,number):
        for n in str(number):
            cal_number = By.CSS_SELECTOR,'#simple{}'.format(n)
            self.base_click(cal_number)

    def page_click_add(self):
        self.base_click(page.cal_add)

    def page_click_eaual(self):
        self.base_click(page.cal_equal)

    def page_get_sum(self):
        return self.base_get_sum(page.cal_result)

    def page_clear(self):
        self.base_click(page.cal_clear)

    def page_get_image(self):
        self.base_get_image()


    def page_cal(self,a,b):
        self.page_click_number(a)
        self.page_click_add()
        self.page_click_number(b)
        self.page_click_eaual()






