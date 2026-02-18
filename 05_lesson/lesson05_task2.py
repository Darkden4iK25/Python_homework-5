from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу
    driver.get("https://uitestingplayground.com/dynamicid")

    # Ждём появления кнопки и кликаем (используем CSS-селектор, так как ID динамический)
    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn")))
    button.click()

finally:
    # Закрываем браузер
    driver.quit()
