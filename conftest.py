import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    """
        Fixture for creating and managing a Selenium WebDriver instance.

        Returns:
            webdriver.Chrome: The WebDriver instance.
        """
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print("\nStarting Chrome for the test")
    driver.maximize_window()

    yield driver  # The WebDriver instance is provided to the test

    # Teardown actions to be performed after the test
    print("\nQuitting the Chrome WebDriver")
    driver.quit()
