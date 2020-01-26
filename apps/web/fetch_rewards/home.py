from selenium.webdriver.common.by import By

from modules.page_object_base import PageObjectBase
from modules.web_control import WebControl
from resources.private.config import FETCH_HOST


class Home(PageObjectBase):
    url = FETCH_HOST
    invite_friends_link = WebControl(By.LINK_TEXT, "Invite Friends")
    careers_link = WebControl(By.LINK_TEXT, "Careers")
