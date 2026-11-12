from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import REG_INPUT_NAME, REG_INPUT_EMAIL, REG_INPUT_PASSWORD, BTN_REGISTER, ERROR_PASSWORD, BASE_URL
from utils import generate_email, generate_password

class TestRegistration:

    def test_registration_success(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(f"{BASE_URL}/register")
        
        driver.find_element(By.XPATH, REG_INPUT_NAME).send_keys("Test User")
        driver.find_element(By.XPATH, REG_INPUT_EMAIL).send_keys(generate_email())
        driver.find_element(By.XPATH, REG_INPUT_PASSWORD).send_keys(generate_password(10))
        driver.find_element(By.XPATH, BTN_REGISTER).click()
        
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    def test_registration_invalid_password(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(f"{BASE_URL}/register")
        
        driver.find_element(By.XPATH, REG_INPUT_NAME).send_keys("Test User")
        driver.find_element(By.XPATH, REG_INPUT_EMAIL).send_keys(generate_email())
        driver.find_element(By.XPATH, REG_INPUT_PASSWORD).send_keys("short")
        driver.find_element(By.XPATH, BTN_REGISTER).click()
        
        error = wait.until(
            EC.visibility_of_element_located((By.XPATH, ERROR_PASSWORD))
        )
        assert "Некорректный пароль" in error.text

    def test_registration_empty_name(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(f"{BASE_URL}/register")
        
        driver.find_element(By.XPATH, REG_INPUT_EMAIL).send_keys(generate_email())
        driver.find_element(By.XPATH, REG_INPUT_PASSWORD).send_keys(generate_password())
        
        driver.find_element(By.XPATH, BTN_REGISTER).click()
        
        assert "/register" in driver.current_url
        
        assert wait.until(
            EC.visibility_of_element_located((By.XPATH, BTN_REGISTER))
        )