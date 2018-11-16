from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class HomePage(BaseAction):

    mine_button = By.XPATH, "//*[@text='我的' and @resource-id='com.tpshop.malls:id/tab_txtv']"

    @allure.step("首页页面-点击-我的按钮")
    def click_mine_button(self):
        self.click(self.mine_button)