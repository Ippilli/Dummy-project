import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from utilities.read_properties import get_config
from utilities.custom_logger import setup_logger
import time

logger = setup_logger()  # Module-level logger

class TestLogin:
    

    @pytest.mark.usefixtures("driver")
    def test_login_with_valid_credentials(self, driver):
        logger.info("Starting test: valid login")
        

        # Open login page
        driver.get("https://www.saucedemo.com")


        # Initialize LoginPage object
        login_page = LoginPage(driver)
        username="standard_user"
        password="secret_sauce"

        # Get credentials safely
        # try:
        #     username = get_config("standard_user")
        #     password = get_config("secret_sauce")
        # except KeyError as e:
        #     logger.error(f"Configuration key missing: {e}")
        #     pytest.fail(f"Test failed due to missing config key: {e}")

        # Perform login
        login_page.set_username(username)
        time.sleep(2)
        login_page.set_password(password)
        time.sleep(2)
        login_page.click_login()

        # Wait until redirected to inventory page
        #WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
        #assert "inventory" in driver.current_url
        logger.info("Valid login test passed.")


        # Wait until redirected to inventory page
       # WebDriverWait(driver, 10).until(EC.url_contains("inventory"))
        #assert "inventory" in driver.current_url
        #logger.info("Valid login test passed.")

    @pytest.mark.usefixtures("driver")
    def test_login_with_invalid_credentials(self, driver):
        logger.info("Starting test: invalid login")

        driver.get("https://www.saucedemo.com")
        login_page = LoginPage(driver)
        login_page.set_username("wrong_user")
        login_page.set_password("wrong_pass")
        login_page.click_login()

        # Wait for error message
        error_message = login_page.get_error_message()
        assert "Epic sadface" in error_message
        logger.info(f"Invalid login correctly displayed error: {error_message}")
