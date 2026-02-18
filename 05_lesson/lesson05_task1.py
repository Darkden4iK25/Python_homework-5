from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Открываем браузер Chrome
driver = webdriver.Chrome()

try:
    # Переходим на страницу с корректным протоколом
    driver.get("https://uitestingplayground.com/classattr")

    # Ждём появления кнопки с явным ожиданием
    wait = WebDriverWait(driver, 10)  # ждём до 10 секунд
    button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn"))
    )

    # Кликаем на кнопку
    button.click()
    print("Кнопка успешно нажата!")

finally:
    # Закрываем браузер
    driver.quit()
