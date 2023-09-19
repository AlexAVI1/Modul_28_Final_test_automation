from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver, url=''):
        self.driver = driver
        self.driver.get(url)

    # Метод поиска элемента на странице.
    def find(self, locator, time=10):
        WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator), message=f"Не удалось найти элемент по локатору {locator}")
        return self.driver.find_element(*locator)

    # Метод переключения на другое окно браузера.
    def switch_window(self, num=-1):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[num])

    # Метод клика по элементу на странице.
    def click(self, locator):
        self.find(locator).click()

    # Метод ввода значения в поле на странице.
    def set(self, locator, value):
        self.find(locator).clear()
        self.find(locator).send_keys(value)

    # Метод получения текста элемента на странице.
    def get_text(self, locator):
        return self.find(locator).text

    # Метод получения текущего URL страницы.
    def get_link(self):
        return self.driver.current_url

