from modules.mobile_driver_base import MobileDriverBase


class LayoutObjectBase(MobileDriverBase):
    def swipe(self, start_x, start_y, end_x, end_y):
        MobileDriverBase.get_driver().swipe(start_x, start_y, end_x, end_y)
