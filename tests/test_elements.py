from conftest import driver
from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            link = "https://demoqa.com/text-box"
            text_box_page = TextBoxPage(driver, link)
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_per_address = text_box_page.check_filled_form()
            assert full_name == output_name, "full names don't match"
            assert email == output_email, "emails don't not match"
            assert current_address == output_cur_address, "current addresses don't not match"
            assert permanent_address == output_per_address, "permanent addresses don't not match"
