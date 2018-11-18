from page.home_page import HomePage
from page.login_page import LoginPage
from page.mine_page import MinePage
from page.setting_page import SettingPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def login(self):
        return LoginPage(self.driver)

    @property
    def setting(self):
        return SettingPage(self.driver)

