from pages.inventory_page import InventoryPage
from utilities.custom_logger import setup_logger

logger = setup_logger()

def test_sort_name_az(login):
    logger.info("Sorting Name A to Z")
    inv = InventoryPage(login)
    inv.select_sort_option("Name (A to Z)")
    names = inv.get_item_names()
    assert names == sorted(names)

def test_sort_name_za(login):
    logger.info("Sorting Name Z to A")
    inv = InventoryPage(login)
    inv.select_sort_option("Name (Z to A)")
    names = inv.get_item_names()
    assert names == sorted(names, reverse=True)

def test_sort_price_low_high(login):
    logger.info("Sorting Price Low to High")
    inv = InventoryPage(login)
    inv.select_sort_option("Price (low to high)")
    prices = inv.get_item_prices()
    assert prices == sorted(prices)

def test_sort_price_high_low(login):
    logger.info("Sorting Price High to Low")
    inv = InventoryPage(login)
    inv.select_sort_option("Price (high to low)")
    prices = inv.get_item_prices()
    assert prices == sorted(prices, reverse=True)
