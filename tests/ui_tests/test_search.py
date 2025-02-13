import pytest
from selenium import webdriver
from config.config import Config


def test_search_product():
    # Initialize WebDriver
    driver = webdriver.Chrome()
    driver.get(Config.BASE_URL)

    try:
        # Basic assertion to verify page loaded
        assert "Your Store" in driver.title
    finally:
        # Ensure browser closes even if test fails
        driver.quit()