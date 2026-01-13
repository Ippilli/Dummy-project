from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.XPATH, "//h3[@data-test='error']")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    # Set username
    def set_username(self, username):
        username_field = self.wait.until(EC.visibility_of_element_located(self.USERNAME))
        username_field.clear()
        username_field.send_keys(username)

    # Set password
    def set_password(self, password):
        password_field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD))
        password_field.clear()
        password_field.send_keys(password)

    # Click login button
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BTN)).click()

    # Convenience method: login in one step
    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login()

    # Get error message
    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.ERROR_MSG)).text
