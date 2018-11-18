from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(by, value))

    def find_elements(self, feature, timeout=10.0, poll=1.0):
        by = feature[0]
        value = feature[1]

        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(by, value))

    def click(self, feature):
        self.find_element(feature).click()

    def input(self, feature, text):
        self.find_element(feature).send_keys(text)

    def is_feature_enabled(self, feature):
        return self.find_element(feature).is_enabled()

    def get_text(self, feature):
        return self.find_element(feature).text

    def is_toast_exist(self, text, is_contains=True):

        toast_feature_value = "//*[contains(@text,'%s')]" % text
        if not is_contains:
            toast_feature_value = "//*[@text='%s']" % text

        try:
            self.find_element((By.XPATH, toast_feature_value), timeout=5, poll=0.5)
            return True
        except Exception:
            return False


