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
            print("登录")
            # 登录
            # 输入用户名
            # 输入xx
            # 点登录

        print("收货地址")
        # 新建地址
        # 添加联系人
        # 添加手机









