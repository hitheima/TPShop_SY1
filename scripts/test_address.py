import time

from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_add_address(self):
        self.page.home.click_mine_button()

        if not self.page.mine.is_login():
            # 我的-登录/注册
            self.page.mine.click_login_and_sign_up()
            # 登录-输入用户名
            self.page.login.input_username("13800138006")
            # 登录-输入密码
            self.page.login.input_password("123456")
            # 登录-点击登录
            self.page.login.click_login()

        print("收货地址")

        time.sleep(10)
        # 新建地址
        # 添加联系人
        # 添加手机









