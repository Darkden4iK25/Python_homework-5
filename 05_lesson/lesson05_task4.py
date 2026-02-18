from selenium import webdriver
from selenium.webdriver.common.by import By

# Открываем браузер Firefox
driver = webdriver.Firefox()

try:
    # Переходим на страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Заполняем поле username
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    # Заполняем поле password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")

    # Нажимаем кнопку Login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Ждём и выводим текст с зелёной плашки
    success_message = driver.find_element(By.CSS_SELECTOR, ".flash.success")
    print(success_message.text.strip())

finally:
    # Закрываем браузер
    driver.quit()
