import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_pages import InventoryPage
from utilities.read_properties import get_config
from utilities.custom_logger import setup_logger

logger = setup_logger()

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

    @pytest.mark.usefixtures("driver")
    def test_login_with_valid_credentials(self, driver):
        logger.info("Starting test: valid login")
        

        # Open login page
        driver.get("https://www.saucedemo.com")


@pytest.fixture
def login(driver):
    driver.get(get_config("base_url", section="environment"))
    login_page = LoginPage(driver)
    login_page.login(get_config("standard_user", section="credentials"),
                     get_config("secret_sauce", section="credentials"))
    return driver

# ----- Login Tests -----
def test_valid_login(login):
    logger.info("Running valid login test")
    assert "inventory" in login.current_url

def test_invalid_login(driver):
    driver.get(get_config("base_url", section="environment"))
    login_page = LoginPage(driver)
    login_page.login("wrong_user", "wrong_pass")
    error_message = login_page.get_error_message()
    logger.info(f"Invalid login error: {error_message}")
    assert "Epic sadface" in error_message

# ----- Dropdown Tests -----
def test_sort_name_az(login):
    inv_page = InventoryPage(login)
    inv_page.select_sort_option("Name (A to Z)")
    names = inv_page.get_item_names()
    assert names == sorted(names)

def test_sort_name_za(login):
    inv_page = InventoryPage(login)
    inv_page.select_sort_option("Name (Z to A)")
    names = inv_page.get_item_names()
    
    assert names == sorted(names, reverse=True)

def test_sort_price_low_high(login):
    inv_page = InventoryPage(login)
    inv_page.select_sort_option("Price (low to high)")
    prices = inv_page.get_item_prices()
    assert prices == sorted(prices)

def test_sort_price_high_low(login):
    inv_page = InventoryPage(login)
    inv_page.select_sort_option("Price (high to low)")
    prices = inv_page.get_item_prices()
    assert prices == sorted(prices, reverse=True)
