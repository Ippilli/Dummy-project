from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class InventoryPage:
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def get_sort_dropdown(self):
        return self.wait.until(EC.visibility_of_element_located(self.SORT_DROPDOWN))

    def select_sort_option(self, option_text):
        select = Select(self.get_sort_dropdown())
        select.select_by_visible_text(option_text)

    def get_item_names(self):
        elements = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_NAMES))
        return [e.text for e in elements]

    def get_item_prices(self):
        elements = self.wait.until(EC.presence_of_all_elements_located(self.ITEM_PRICES))
        return [float(e.text.replace("$", "")) for e in elements]
