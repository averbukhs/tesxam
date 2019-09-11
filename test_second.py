from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

hostname = 'https://demo.b2b-center.ru/personal/'
login = '51370'
password = 'Password8'


"""
Тест на заполнение формы корректными данными. Тест является пройденным при проверке на наличии фразы "Личный кабинет"
в заголовке Title после нажатия кнопки Войти.
"""

def test_input_login_password_correct(driver):

    driver.get(hostname)
    wait = WebDriverWait(driver, 10)

    assert "B2B-Center" in driver.title

    login_field = driver.find_element(By.ID, value="login_control")
    password_field = driver.find_element(By.ID, value="password_control")
    submit_button = driver.find_element(By.ID, value="enter_button")

    login_field.send_keys(login)
    password_field.send_keys(password)
    submit_button.click()
    try:
        element = wait.until(EC.title_contains("Личный кабинет"))
    finally:
        assert "Личный кабинет" in driver.title
