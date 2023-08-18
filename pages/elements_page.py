from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
import time


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.FULL_NAME).send_keys("Name")
        self.element_is_visible(self.locators.EMAIL).send_keys("email@e.com")
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys("cur address")
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys("perm address")
        self.element_is_visible(self.locators.SUBMIT).click()
        time.sleep(5)
