from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:

    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_sort_option(self, option_text):
        dropdown = self.wait.until(EC.element_to_be_clickable(self.SORT_DROPDOWN))
        Select(dropdown).select_by_visible_text(option_text)

    def get_item_names(self):
        items = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAMES))
        return [item.text for item in items]

    def get_item_prices(self):
        prices = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_PRICES))
        return [float(price.text.replace("$", "")) for price in prices]
