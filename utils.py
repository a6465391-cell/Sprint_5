import random
import string
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def generate_email():
    letters = "".join(random.choices(string.ascii_lowercase, k=8))
    return f"{letters}@example.com"

def generate_password(length=8):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))

def dismiss_modal_if_present(driver, timeout=5):
    """Закрывает модальное окно, если оно открыто. timeout — секунды."""
    try:
        close_button = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located(
                (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
            )
        )
        close_button.click()
    except TimeoutException:
        pass
    
  

