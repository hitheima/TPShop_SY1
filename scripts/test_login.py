import time

from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login(self):
        # 首页-我的
        self.page.home.click_mine_button()
        # 我的-登录/注册
        self.page.mine.click_login_and_sign_up()


