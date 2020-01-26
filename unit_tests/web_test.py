import unittest
from apps.web.fetch_rewards.home import Home


class MyTestCase(unittest.TestCase):
    def test_careers_link(self):
        home = Home()
        home.navigate_to(home.url)
        home.invite_friends_link.click()
        home.careers_link.click()
        self.assertEqual(home.get_current_url(), home.url + "careers")
        home.close_browser()


if __name__ == '__main__':
    unittest.main()
