from modules.web_driver_base import WebDriverBase


class WebControl(WebDriverBase):
    def __init__(self, by, value):
        super().__init__()
        self.element = None
        self.by = by
        self.value = value

    def find_element(self):
        return self.get_driver().find_element(self.by, self.value)

    def click(self):
        self.find_element().click()

    def send_keys(self, text):
        self.find_element().send_keys(text)

    def get_text(self):
        return self.find_element().text
