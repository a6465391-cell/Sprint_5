from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import (LINK_PROFILE, LINK_CONSTRUCTOR, LOGO_STELLAR, BASE_URL, MODAL_OVERLAY, MODAL_CLOSE)

class TestNavigation:
    """Класс для тестов навигации"""

    @staticmethod
    def _close_modal_if_present(wait):
        """Статический метод для закрытия модального окна (не требует self)"""
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, MODAL_CLOSE))).click()
        except TimeoutException:
            pass  
        try:
            wait.until(EC.invisibility_of_element_located((By.XPATH, MODAL_OVERLAY)))
        except TimeoutException:
            pass

    def test_go_to_profile(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL)
        self._close_modal_if_present(wait)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, LINK_PROFILE))).click()
        wait.until(lambda d: "/login" in d.current_url or "/account" in d.current_url)
        assert "/login" in driver.current_url or "/account" in driver.current_url

    def test_go_to_constructor_via_menu(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL + "/login")
        self._close_modal_if_present(wait)
        
        wait.until(EC.element_to_be_clickable((By.XPATH, LINK_CONSTRUCTOR))).click()
        wait.until(lambda d: d.current_url.rstrip("/") == BASE_URL.rstrip("/"))
        assert driver.current_url.rstrip("/") == BASE_URL.rstrip("/")

    def test_go_to_constructor_via_logo(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL + "/login")
        self._close_modal_if_present(wait)
        
        logo = wait.until(EC.element_to_be_clickable((By.XPATH, LOGO_STELLAR)))
        logo.click()
        wait.until(lambda d: d.current_url.rstrip("/") == BASE_URL.rstrip("/"))
        assert driver.current_url.rstrip("/") == BASE_URL.rstrip("/")
