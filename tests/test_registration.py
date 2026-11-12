from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from locators import REG_INPUT_NAME, REG_INPUT_EMAIL, REG_INPUT_PASSWORD, BTN_REGISTER, ERROR_PASSWORD, BASE_URL
from utils import generate_email, generate_password

def test_registration_success(driver):
    driver.get(f"{BASE_URL}/register")
    driver.find_element(By.XPATH, REG_INPUT_NAME).send_keys("Test User")
    driver.find_element(By.XPATH, REG_INPUT_EMAIL).send_keys(generate_email())
    driver.find_element(By.XPATH, REG_INPUT_PASSWORD).send_keys(generate_password(10))
    driver.find_element(By.XPATH, BTN_REGISTER).click()

def test_registration_invalid_password(driver):
    driver.get(f"{BASE_URL}/register")
    driver.find_element(By.XPATH, REG_INPUT_NAME).send_keys("Test User")
    driver.find_element(By.XPATH, REG_INPUT_EMAIL).send_keys(generate_email())
    driver.find_element(By.XPATH, REG_INPUT_PASSWORD).send_keys("short")
    driver.find_element(By.XPATH, BTN_REGISTER).click()
    error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, ERROR_PASSWORD))
    )
    assert "Некорректный пароль" in error.text

def test_registration_empty_name(driver):
    driver.get(f"{BASE_URL}/register")

    # Заполняем всё, кроме имени
    driver.find_element(By.XPATH, REG_INPUT_EMAIL).send_keys(generate_email())
    driver.find_element(By.XPATH, REG_INPUT_PASSWORD).send_keys(generate_password())

    # Пытаемся зарегистрироваться с пустым именем
    driver.find_element(By.XPATH, BTN_REGISTER).click()

    # Проверки того, что «ничего не произошло»:
    # 1. Мы остались на странице регистрации
    assert "/register" in driver.current_url

    # 2. Кнопка регистрации всё ещё на месте — форма не ушла
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, BTN_REGISTER))
    )

