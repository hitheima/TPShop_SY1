import random
import time

import pytest

from base.base_driver import init_driver
from page.page import Page
from base.base_analyze import analyze_file


def random_number():
    number = ""
    for _ in range(8):
        number += str(random.randint(0, 9))
    return number


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

    @pytest.mark.parametrize("args", analyze_file("login_data.yml", "test_login_miss_part"))
    def test_login_miss_part(self, args):
        # # 准备数据
        username = args["username"]
        password = args["password"]

        # 首页-我的
        self.page.home.click_mine_button()
        # 我的-登录/注册
        self.page.mine.click_login_and_sign_up()
        # 登录-输入用户名
        self.page.login.input_username(username)
        # 登录-输入密码
        self.page.login.input_password(password)

        assert not self.page.login.is_login_button_enabled()


        # # 断言，如果按钮不可用，则通过。如果按钮可用，则不通过。
        # if self.page.login.is_login_button_enabled() == False:
        #     assert True
        # else:
        #     assert False

        # assert not self.page.login.is_login_button_enabled()

        # 如果数据设计的时候，没有不输入的key，使用下面的写法
        # if "username" in args:
        #     # 登录-输入用户名
        #     self.page.login.input_username(args["username"])
        #
        # if "password" in args:
        #     # 登录-输入密码
        #     self.page.login.input_password(args["password"])

    @pytest.mark.parametrize("input_pwd", [random_number(), random_number()])
    def test_show_password(self, input_pwd):

        # 首页-我的
        self.page.home.click_mine_button()
        # 我的-登录/注册
        self.page.mine.click_login_and_sign_up()

        # 登录-输入密码
        self.page.login.input_password(input_pwd)
        # 密码是不是没有显示，如果是
        if self.page.login.get_password_text() == input_pwd:
            assert False, "password上的文字在没现实面之前就显示了，不正常"

        # 点击显示密码按钮
        self.page.login.click_show_password()
        # sleep看到效果
        time.sleep(2)

        # 断言，密码框中的文字是不是和之前输入的一致
        assert input_pwd == self.page.login.get_password_text()

