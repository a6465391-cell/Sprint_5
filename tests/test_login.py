from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import (BTN_LOGIN_ON_HOME, LINK_PROFILE, REG_LINK_LOGIN, LOGIN_LINK_RECOVER, BASE_URL)
from utils import dismiss_modal_if_present

WAIT = 10

def test_login_via_home(driver):
    wait = WebDriverWait(driver, WAIT)
    driver.get(BASE_URL)
    dismiss_modal_if_present(driver)
    wait.until(EC.element_to_be_clickable((By.XPATH, BTN_LOGIN_ON_HOME))).click()
    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url


def test_login_via_profile(driver):
    wait = WebDriverWait(driver, WAIT)
    driver.get(BASE_URL)
    # ВАЖНО: сначала гасим модалку, потом кликаем
    dismiss_modal_if_present(driver)
    wait.until(EC.element_to_be_clickable((By.XPATH, LINK_PROFILE))).click()
    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url


def test_login_from_registration(driver):
    wait = WebDriverWait(driver, WAIT)
    driver.get(BASE_URL + "/register")
    dismiss_modal_if_present(driver)
    wait.until(EC.element_to_be_clickable((By.XPATH, REG_LINK_LOGIN))).click()
    wait.until(EC.url_contains("/login"))
    assert "/login" in driver.current_url


def test_login_from_recovery(driver):
    wait = WebDriverWait(driver, WAIT)
    driver.get(BASE_URL + "/login")
    dismiss_modal_if_present(driver)
    wait.until(EC.element_to_be_clickable((By.XPATH, LOGIN_LINK_RECOVER))).click()
    wait.until(EC.url_contains("/forgot-password"))
    assert "/forgot-password" in driver.current_url
