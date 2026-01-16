import pytest
from selenium import webdriver
from pages.login_page import LoginPage

@pytest.fixture(scope="session")
def login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Step 1: Open login page
    driver.get("https://www.saucedemo.com")

    # Step 2: Login
    LoginPage(driver).login("standard_user", "secret_sauce")

    # Step 3: Verify navigation to next page
    assert "inventory" in driver.current_url

    yield driver
    driver.quit()
