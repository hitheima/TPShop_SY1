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

    def scroll_page_one_time(self, direction="up"):
        """
        滑动当前屏幕一次
        :param direction:
            "up"：从下往上
            "down"：从上往下
            "left"：从右往左
            "right"：从左往右
        :return:
        """
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        center_x = screen_width * 0.5
        center_y = screen_height * 0.5

        top_x = center_x
        top_y = screen_height * 0.25
        bottom_x = center_x
        bottom_y = screen_height * 0.75
        left_x = screen_width * 0.25
        left_y = center_y
        right_x = screen_width * 0.75
        right_y = center_y

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y)
        else:
            raise Exception("请输入正确的参数，up/down/left/right")

    def is_feature_exist_scroll_page(self, feature, direction="up"):
        old_source = ""
        while True:
            try:
                old_source = self.driver.page_source
                self.find_element(feature)
                return True
            except Exception:
                self.scroll_page_one_time(direction)
                if old_source == self.driver.page_source:
                    return False




