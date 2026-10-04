from selenium.webdriver.common.by import By

class OrderPageLocators:
    # --- ЭКРАН 1: Для кого самокат ---
    INPUT_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    INPUT_SURNAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    
    # Динамический локатор для выбора конкретной станции из выпадающего списка
    @staticmethod
    def metro_station(station_name):
        return (By.XPATH, f".//li[@class='select-search__row']//div[text()='{station_name}']")
    
    INPUT_PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']")

    # --- ЭКРАН 2: Про аренду ---
    # Дата аренды
    INPUT_DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")    
    # Сроки аренды
    INPUT_RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-placeholder")
    RENTAL_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option') and text()='{}']")

    # Чекбоксы цветов
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    
    INPUT_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER_FINAL = (By.XPATH, ".//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']")

    # --- МОДАЛЬНОЕ ОКНО ПОДТВЕРЖДЕНИЯ ---
    BUTTON_YES = (By.XPATH, ".//button[text()='Да']")
    
    # Заголовок окна успешного заказа ("Заказ оформлен")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'Заказ оформлен')]")

    # Выносим ШАБЛОН локатора. Переменная {day} будет подставлена позже. 
    DATE_CELL_TEMPLATE = "//div[contains(@class, 'react-datepicker__day') and text()='{day}']"