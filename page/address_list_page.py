from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class AddressListPage(BaseAction):

    add_address = By.ID, "com.tpshop.malls:id/add_address_btn"

    @allure.step("收货人地址页面-点击-新建地址按钮")
    def click_add_address(self):
        self.click(self.add_address)