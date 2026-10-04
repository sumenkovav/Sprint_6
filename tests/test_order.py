import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder:

    @allure.title("Проверка флоу позитивного сценария заказа самоката")

    @allure.description("Проверяем весь путь оформления заказа через разные точки входа с разными наборами данных")

    @pytest.mark.parametrize(
        "entry_point, name, surname, address, metro_station, phone, date, rent_time, color, comment",
        [
            # Набор №1: Верхняя кнопка, Черный самокат
            ("top", "Александр", "Суменков", "ул. Пушкина, д. 1", "Митино", "79991234567", "10.10.2026", "сутки", "black", "Позвонить за час"),
            # Набор №2: Нижняя кнопка, Серый самокат
            ("bottom", "Снежана", "Зимняя", "ул. Гоголя, д. 2, кв. 1", "Фрунзенская", "89997654321", "20.10.2026", "двое суток", "grey", "")
        ]
    )

    def test_scooter_order_flow(self, driver, entry_point, name, surname, address, metro_station, phone, date, rent_time, color, comment):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        
        # Шаг 1: Открываем сайт и принимаем куки
        main_page.open_main_page()
        main_page.accept_cookies()
        
        # Шаг 2: Выбираем точку входа на основании параметров теста
        main_page.click_order_button(entry_point)
            
        # Шаг 3: Заполняем личные данные (Экран 1) - вызываем существующие методы по очереди 
        order_page.fill_name(name) 
        order_page.fill_surname(surname) 
        order_page.fill_address(address) 
        order_page.select_metro(metro_station) 
        order_page.fill_phone(phone)
        order_page.click_next()
        
        # Шаг 4: Заполняем данные аренды (Экран 2)
        order_page.select_date(date) 
        order_page.select_rental_period(rent_time)
        # Выбор цвета (так как методов два, используем условие) 
        order_page.select_color(color)
        # Заполнение комментария
        order_page.fill_comment(comment)
        
        # Шаг 5: Подтверждаем заказ в поп-апе
        order_page.click_order()
        
        # Шаг 6: Проверяем, что появилось окно успешного заказа
        assert order_page.is_success_displayed(), "Модальное окно 'Заказ оформлен' не появилось"
