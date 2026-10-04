import pytest
import allure
from pages.main_page import MainPage
from urls import Urls

class TestLogos:

    @allure.title("Проверка клика на логотип «Самоката»")
    @allure.description("Проверяем, что при клике на логотип «Самоката» со страницы заказа происходит переход на главную страницу")
    def test_scooter_logo_navigates_to_home(self, driver):
        main_page = MainPage(driver)
        
        # Шаг 1: Открываем главную и переходим на страницу заказа, чтобы уйти с главной
        main_page.open_main_page()
        main_page.accept_cookies()
        main_page.click_header_order_button()
        
        # Шаг 2: Кликаем на логотип Самоката
        main_page.click_scooter_logo()
        
        # Шаг 3: Проверяем, что URL снова стал главной страницей
        assert main_page.get_current_url() == Urls.SCOOTER_MAIN_PAGE, f"Ожидали URL {Urls.SCOOTER_MAIN_PAGE}"

    @allure.title("Проверка клика на логотип Яндекса и перехода на Дзен")
    @allure.description("Проверяем, что клик на логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_redirects_to_dzen(self, driver):
        main_page = MainPage(driver)
        
        # Шаг 1: Открываем главную страницу
        main_page.open_main_page()
        main_page.accept_cookies()
        
        # Шаг 2: Кликаем на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Шаг 3: Переключаемся на новую вкладку
        main_page.switch_to_new_tab()
        
        # Шаг 4: Ждем нужный URL
        main_page.wait_for_url_contains(Urls.DZEN_HOME_PAGE_PART)
        
        # Шаг 5: Проверяем, что мы на Дзене
        assert Urls.DZEN_HOME_PAGE_PART in main_page.get_current_url(), "Переход на dzen.ru не произошел"
