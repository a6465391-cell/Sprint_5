from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils import generate_email, generate_password
from locators import (BASE_URL, REG_INPUT_NAME, REG_INPUT_EMAIL, REG_INPUT_PASSWORD, BTN_REGISTER, INPUT_LOGIN_EMAIL1, INPUT_LOGIN_PASSWORD1, BTN_LOGIN, BTN_LOGOUT)

def test_logout(driver):
    wait = WebDriverWait(driver, 10)

    driver.get(f"{BASE_URL}/register")
    email = generate_email()
    password = generate_password()
    driver.find_element(By.XPATH, REG_INPUT_NAME).send_keys("Test User")
    driver.find_element(By.XPATH, REG_INPUT_EMAIL).send_keys(email)
    driver.find_element(By.XPATH, REG_INPUT_PASSWORD).send_keys(password)
    driver.find_element(By.XPATH, BTN_REGISTER).click()

    wait.until(EC.url_contains("/login"))

    email_input = wait.until(EC.element_to_be_clickable((By.XPATH, INPUT_LOGIN_EMAIL1)))
    email_input.click()
    email_input.clear()
    email_input.send_keys(email)
    pass_input = wait.until(EC.element_to_be_clickable((By.XPATH, INPUT_LOGIN_PASSWORD1)))
    pass_input.click()
    pass_input.clear()
    pass_input.send_keys(password)

    wait.until(EC.element_to_be_clickable((By.XPATH, BTN_LOGIN))).click()

    wait.until(lambda d: "/login" not in d.current_url)

    profile_link = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")))
    profile_link.click()
    wait.until(EC.url_contains("/account"))

    wait.until(EC.element_to_be_clickable((By.XPATH, BTN_LOGOUT))).click()

    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url