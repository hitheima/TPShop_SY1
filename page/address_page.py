from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class AddressPage(BaseAction):

    name_edit_text = By.ID, "com.tpshop.malls:id/consignee_name_edtv"

    mobile_edit_text = By.ID, "com.tpshop.malls:id/consignee_mobile_edtv"

    address_edit_text = By.ID, "com.tpshop.malls:id/consignee_address_edtv"

    region_button = By.ID, "com.tpshop.malls:id/consignee_region_txtv"

    save_address_button = By.XPATH, "//*[@text='保存收货地址']"

    @allure.step("收货地址页面-输入-收货人")
    def input_name(self, text):
        self.input(self.name_edit_text, text)

    @allure.step("收货地址页面-输入-手机号码")
    def input_mobile(self, text):
        self.input(self.mobile_edit_text, text)

    @allure.step("收货地址页面-输入-详细地址")
    def input_address(self, text):
        self.input(self.address_edit_text, text)

    @allure.step("收货地址页面-点击-所在地区")
    def click_region(self):
        self.click(self.region_button)

    def click_save_address(self):
        self.click(self.save_address_button)
