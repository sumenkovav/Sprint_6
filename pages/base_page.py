import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Открываем страницу: {url}")
    def open_page(self, url):
        self.driver.get(url)

    @allure.step("Ожидаем появления элемента в DOM")
    def find_element_with_wait(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    @allure.step("Ожидаем, пока элемент станет кликабельным")
    def wait_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        ) 

    @allure.step("Ожидаем видимости элемента на странице")
    def wait_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step("Проверить, виден ли элемент (возвращает True/False)")
    def is_element_visible(self, locator, timeout=10):
        """Возвращает True, если элемент виден, иначе False."""
        try:
            # Используем тот же механизм ожидания, что и в wait_element_to_be_visible,
            # но оборачиваем в try-except, чтобы не падать с ошибкой, а вернуть False.
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )
            return True
        except Exception:
            return False 
    
    @allure.step("Прокручиваем страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликнуть по элементу с локатором {locator}")
    def click(self, locator):
        """Кликает по элементу после ожидания его кликабельности."""
        element = self.wait_element_to_be_clickable(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в поле с локатором {locator}")
    def send_keys(self, locator, text):
        """Вводит текст в найденный элемент."""
        element = self.wait_element_to_be_clickable(locator)
        element.clear()  # Очищаем поле перед вводом (хорошая практика)
        element.send_keys(text) 

    @allure.step("Получаем текст элемента")
    def get_element_text(self, locator):
        return self.wait_element_to_be_visible(locator).text

    @allure.step("Получаем текущий URL страницы")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Переключаемся на новую вкладку браузера")
    def switch_to_new_tab(self):
        # Ждем, пока вкладок станет больше одной
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        # Переключаемся на вторую вкладку (индекс 1)
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)

    @allure.step("Ожидаем, пока URL будет содержать текст: {text}")
    def wait_for_url_contains(self, text, time=10):
        WebDriverWait(self.driver, time).until(EC.url_contains(text))
        