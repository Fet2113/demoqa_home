from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SwagLabs(BasePage):
    def exist_icon(self):
        try:
            self.find_element(locator="div.login_logo")
        except NoSuchElementException:
            return  False
        return  True
    def click_on_the_icon(self):
        self.find_element(locator="div.login_logo").click()
    def input(self):
        self.find_element(locator="#user-name").click()
    def input(self):
        self.find_element(locator="#password").click()
