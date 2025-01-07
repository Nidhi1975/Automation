import pytest
from utils.webdriver_manager import WebDriverFactory

@pytest.fixture(scope="function")
def driver():
    driver = WebDriverFactory.get_driver()
    yield driver
    driver.quit()