from cal.po1 import page
from cal.po1.base.base import CalBase

class PageCal(CalBase):

    def page_click_value(self):
        self.base_click(page.cal_value)

    def page_get_text(self):
        return self.base_get_sum_value(page.cal_text)

    def page_get_image(self):
        self.base_get_image()

    def page_cal(self):
        self.page_click_value()
        self.page_click_value()



