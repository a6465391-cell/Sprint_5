import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TAB_BUNS, TAB_SAUCES, TAB_FILLINGS, TAB_BUNS_ACTIVE, TAB_SAUCES_ACTIVE, TAB_FILLINGS_ACTIVE, MODAL_OVERLAY, MODAL_CLOSE, BASE_URL

class TestConstructor:

    def _close_modal_if_present(self, wait):
        try:
            wait.until(EC.element_to_be_clickable((By.XPATH, MODAL_CLOSE))).click()
            wait.until(EC.invisibility_of_element_located((By.XPATH, MODAL_OVERLAY)))
        except Exception:
            pass

    @pytest.mark.parametrize("tab_locator, active_locator", [
        (TAB_BUNS, TAB_BUNS_ACTIVE),
        (TAB_SAUCES, TAB_SAUCES_ACTIVE),
        (TAB_FILLINGS, TAB_FILLINGS_ACTIVE)
    ])
    def test_switch_tab(self, driver, tab_locator, active_locator):
        wait = WebDriverWait(driver, 10)
        driver.get(BASE_URL)
        self._close_modal_if_present(wait)

        element = wait.until(EC.element_to_be_clickable((By.XPATH, tab_locator)))
        
        ActionChains(driver).move_to_element(element).pause(1).click().perform()
        
        active_marker = wait.until(EC.presence_of_element_located((By.XPATH, active_locator)))
        
        assert active_marker.is_displayed(), f"Вкладка не активировалась: {active_locator}"

