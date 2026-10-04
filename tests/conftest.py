import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Инициализируем Firefox
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    yield driver
    
    # Закрываем браузер после теста
    driver.quit()