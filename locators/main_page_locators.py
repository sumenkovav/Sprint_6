from selenium.webdriver.common.by import By

class MainPageLocators:
    # Кнопка согласия на куки (имеет стабильный ID)
    COOKIE_ACCEPT_BUTTON = (By.ID, 'rcc-confirm-button')
    
    # Сам блок аккордеона FAQ (чтобы до него скроллить)
    FAQ_BLOCK = (By.CLASS_NAME, 'accordion')

    # Кнопки заказа (используем частичное совпадение классов через XPath)
    HEADER_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    BOTTOM_ORDER_BUTTON = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")
    
    # Логотипы (для следующих тестов)
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")

    # Динамический генератор локатора для вопроса (кнопки) по его индексу (0-7)
    @staticmethod
    def get_question_locator(index):
        return (By.ID, f'accordion__heading-{index}')

    # Динамический генератор локатора для ответа (панели с текстом) по индексу (0-7)
    @staticmethod
    def get_answer_locator(index):
        return (By.ID, f'accordion__panel-{index}') 