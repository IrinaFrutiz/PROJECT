import time
from conftest import driver
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            link = "https://demoqa.com/text-box"
            page = TextBoxPage(driver, link)
            page.open()
            full_name, email, current_address, permanent_address = page.fill_all_fields()
