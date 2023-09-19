import pytest
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage

# Инициализации драйвера
@pytest.fixture(params=["chrome"])
def initialize_driver(request):

    if request.param == "chrome":
        driver = webdriver.Chrome()

    request.cls.driver = driver
    print("Browser: ", request.param)
    driver.maximize_window()
    yield
    print("\nClose Driver")
    driver.close()
    driver.quit()


@pytest.fixture()
def auth_page(request, initialize_driver):
    auth_page = AuthPage(request.cls.driver)
    return auth_page


def pytest_configure(config):
    config.addinivalue_line("markers", "skip_if_captcha: mark test as skipped if CAPTCHA is present on the page")


@pytest.fixture(autouse=True)
def check_captcha(request, auth_page):
    marker = request.node.get_closest_marker("skip_if_captcha")
    if marker:
        try:
            captcha_element = auth_page.find((By.CLASS_NAME, 'rt-captcha__image-con'))
            if captcha_element.is_displayed():
                pytest.skip("CAPTCHA is present on the page")
        except TimeoutException:
            pass


