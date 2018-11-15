from page.home_page import HomePage
from page.mine_page import MinePage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)