import time

import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_file


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_file("login_data.yml", "test_login"))
    def test_login(self, args):
        # 准备数据
        username = args["username"]
        password = args["password"]
        hint = args["hint"]

        # 首页-我的
        self.page.home.click_mine_button()
        # 我的-登录/注册
        self.page.mine.click_login_and_sign_up()
        # 登录-输入用户名
        self.page.login.input_username(username)
        # 登录-输入密码
        self.page.login.input_password(password)
        # 登录-点击登录
        self.page.login.click_login()

        # 断言
        assert self.page.login.is_toast_exist(hint)

