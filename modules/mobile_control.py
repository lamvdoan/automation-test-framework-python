from modules.mobile_driver_base import MobileDriverBase
from modules.by import By


class MobileControl(MobileDriverBase):
    def __init__(self, by, value):
        super().__init__()
        self.element = None
        self.by = by
        self.value = value

    def find_element(self):
        if self.by == By.ID:
            return self.get_driver().find_element_by_id(self.value)
        elif self.by == By.CLASS:
            return self.get_driver().find_element_by_class_name(self.value)
        elif self.by == By.LINK_TEXT:
            return self.get_driver().find_element_by_link_text(self.value)
        elif self.by == By.X_PATH:
            return self.get_driver().find_element_by_xpath(self.value)

    def click(self):
        self.find_element().click()

    def send_keys(self, text):
        self.find_element().send_keys(text)

    def get_text(self):
        return self.find_element().text
