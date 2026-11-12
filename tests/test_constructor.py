from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from locators import (TAB_BUNS, TAB_SAUCES, TAB_FILLINGS, TAB_BUNS_ACTIVE, TAB_SAUCES_ACTIVE, TAB_FILLINGS_ACTIVE, MODAL_OVERLAY, MODAL_CLOSE, BASE_URL)

def close_modal_if_present(driver, wait):
    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, MODAL_CLOSE))).click()
    except TimeoutException:
        pass
    try:
        wait.until(EC.invisibility_of_element_located((By.XPATH, MODAL_OVERLAY)))
    except TimeoutException:
        pass


def test_constructor(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(BASE_URL)
    close_modal_if_present(driver, wait)

    tabs = [(TAB_BUNS, TAB_BUNS_ACTIVE), (TAB_SAUCES, TAB_SAUCES_ACTIVE), (TAB_FILLINGS, TAB_FILLINGS_ACTIVE)]
    for tab_xpath, active_xpath in tabs:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, tab_xpath)))
        ActionChains(driver).move_to_element(element).pause(1).click().perform()
        wait.until(EC.presence_of_element_located((By.XPATH, active_xpath)))
