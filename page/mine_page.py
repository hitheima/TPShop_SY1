from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class MinePage(BaseAction):

    login_and_sign_up_button = By.XPATH, "//*[@text='登录/注册']"

    setting_button = By.ID, "com.tpshop.malls:id/setting_btn"

    title_feature = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

    @allure.step("我的页面-点击-登录/注册")
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up_button)

    @allure.step("我的页面-点击-设置")
    def click_setting(self):
        self.click(self.setting_button)

    def is_login(self):
        self.click_setting()
        res = self.get_text(self.title_feature)
        self.driver.press_keycode(4)
        if "登录" == res:
            return False
        return True


