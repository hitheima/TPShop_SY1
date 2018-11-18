import random
import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction
import allure


class RegionPage(BaseAction):

    city_feature = By.ID, "com.tpshop.malls:id/tv_city"

    commit_button = By.XPATH, "//*[@text='确定']"

    def click_city(self):
        for _ in range(4):
            cities = self.find_elements(self.city_feature)
            random_city_index = random.randint(0, len(cities) - 1)
            cities[random_city_index].click()
            time.sleep(1)

    def click_commit(self):
        self.click(self.commit_button)


