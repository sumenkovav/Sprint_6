import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from urls import Urls

class MainPage(BasePage):
    
    @allure.step("Открываем главную страницу Самоката")
    def open_main_page(self):
        self.open_page(Urls.SCOOTER_MAIN_PAGE)
        
    @allure.step("Принимаем куки, если баннер отображается")
    def accept_cookies(self):
        self.click(MainPageLocators.COOKIE_ACCEPT_BUTTON)

    @allure.step("Скроллим до блока FAQ («Вопросы о важном»)")
    def scroll_to_faq(self):
        self.scroll_to_element(MainPageLocators.FAQ_BLOCK)

    @allure.step("Кликаем по вопросу №{index}")
    def click_faq_question(self, index):
        locator = MainPageLocators.get_question_locator(index)
        self.click(locator)

    @allure.step("Получаем текст ответа №{index}")
    def get_faq_answer_text(self, index):
        locator = MainPageLocators.get_answer_locator(index)
        return self.get_element_text(locator)
    
    @allure.step("Кликаем по верхней кнопке «Заказать» в шапке")
    def click_header_order_button(self):
        self.click(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step("Кликаем по нижней кнопке «Заказать»")
    def click_bottom_order_button(self):
        self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
        self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)

    @allure.step("Кликаем на логотип «Самоката»")
    def click_scooter_logo(self):
        self.click(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.click(MainPageLocators.YANDEX_LOGO)

    @allure.step("Нажать кнопку заказа с точкой входа '{entry_point}'")
    def click_order_button(self, entry_point):
        """Нажимает кнопку заказа в зависимости от типа точки входа."""
        if entry_point == "top":
            self.click(MainPageLocators.HEADER_ORDER_BUTTON)            
        elif entry_point == "bottom":
            self.scroll_to_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
            self.click(MainPageLocators.BOTTOM_ORDER_BUTTON)            
        else:
            raise ValueError(f"Неизвестная точка входа: {entry_point}")  
