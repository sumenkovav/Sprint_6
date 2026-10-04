from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import allure
from locators.order_page_locators import OrderPageLocators



class OrderPage(BasePage):
    """Класс для страницы заказа самоката."""

    def __init__(self, driver):
        """Инициализация страницы заказа."""
        super().__init__(driver)
        self.locators = OrderPageLocators

    @allure.step("Кликнуть по кнопке 'Заказать' в верхней части страницы")
    def click_order_button_top(self):
        """Кликает по кнопке 'Заказать' в верхней части страницы."""
        self.click(self.locators.ORDER_BUTTON_TOP)

    @allure.step("Кликнуть по кнопке 'Заказать' в нижней части страницы")
    def click_order_button_bottom(self):
        """Кликает по кнопке 'Заказать' в нижней части страницы."""
        self.click(self.locators.ORDER_BUTTON_BOTTOM)

    @allure.step("Заполнить поле 'Имя' значением '{name}'")
    def fill_name(self, name):
        """Заполняет поле 'Имя'."""
        self.send_keys(self.locators.INPUT_NAME, name)

    @allure.step("Заполнить поле 'Фамилия' значением '{surname}'")
    def fill_surname(self, surname):
        """Заполняет поле 'Фамилия'."""
        self.send_keys(self.locators.INPUT_SURNAME, surname)

    @allure.step("Заполнить поле 'Адрес' значением '{address}'")
    def fill_address(self, address):
        """Заполняет поле 'Адрес'."""
        self.send_keys(self.locators.INPUT_ADDRESS, address)

    @allure.step("Заполнить поле 'Телефон' значением '{phone}'")
    def fill_phone(self, phone):
        """Заполняет поле 'Телефон'."""
        self.send_keys(self.locators.INPUT_PHONE, phone)

    @allure.step("Выбрать станцию метро '{station}'")
    def select_metro(self, station):
        """Выбирает станцию метро из выпадающего списка."""
        self.click(self.locators.INPUT_METRO)
        self.click(self.locators.metro_station(station))

    @allure.step("Выбрать дату '{day}' в календаре")
    def select_date(self, day):
        """Выбирает дату, кликая по ячейке с числом"""    
    # Открываем календарь
        self.click(self.locators.INPUT_DATE)    
    # Берем из даты только ДЕНЬ (число)
        day_number = day.split('.')[0].lstrip('0')    
    # Используем шаблон из локаторов 
    # Мы берем шаблон и форматируем его, получая готовый локатор 
        xpath_string = self.locators.DATE_CELL_TEMPLATE.format(day=day_number) 
        locator = (By.XPATH, xpath_string)
    # Ждем и кликаем 
        element = self.wait_element_to_be_clickable(locator, timeout=15) 
        self.click(element)

    @allure.step("Выбрать срок аренды '{period}'")
    def select_rental_period(self, period):
        """Выбирает срок аренды из выпадающего списка."""
        self.click(self.locators.INPUT_RENTAL_PERIOD)
        locator = (self.locators.RENTAL_OPTION[0], self.locators.RENTAL_OPTION[1].format(period))
        self.click(locator)

    @allure.step("Выбрать цвет самоката '{color}'")
    def select_color(self, color):
        """Выбирает цвет самоката. Принимает 'black' или 'grey'."""
        if color == "black":
            self.click(self.locators.COLOR_BLACK)
        elif color == "grey":
            self.click(self.locators.COLOR_GREY)
        else:
            raise ValueError(f"Неизвестный цвет: {color}") 

    @allure.step("Заполнить поле комментария текстом '{comment}'") 
    def fill_comment(self, comment): 
        self.send_keys(self.locators.INPUT_COMMENT, comment) 

    @allure.step("Нажать кнопку 'Далее'")
    def click_next(self):
        """Нажимает кнопку 'Далее' для перехода ко второй части формы."""
        self.click(self.locators.BUTTON_NEXT)

    def click_order(self):
        """Нажимает кнопку 'Заказать' и обрабатывает всплывающее окно браузера."""        
        self.click(self.locators.BUTTON_ORDER_FINAL)        
        try:
            confirm_button_locator = (By.XPATH, "//button[text()='Да']")
            self.wait_element_to_be_clickable(confirm_button_locator, timeout=10)
            self.click(confirm_button_locator)
        except Exception:
            pass 

    @allure.step("Подтвердить заказ (кнопка 'Да')")
    def click_yes(self):
        """Подтверждает заказ в модальном окне (кнопка 'Да')."""
        self.click(self.locators.BUTTON_YES)

    @allure.step("Получить текст сообщения об успешном заказе")
    def get_success_message(self):
        """Возвращает текст сообщения об успешном оформлении заказа."""
        return self.get_text(self.locators.SUCCESS_MESSAGE)

    @allure.step("Проверить, отображается ли сообщение об успешном заказе")
    def is_success_displayed(self):
        """Проверяет, отображается ли сообщение об успешном заказе."""
        return self.is_element_visible(self.locators.SUCCESS_MESSAGE)
