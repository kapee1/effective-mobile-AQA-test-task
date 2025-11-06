import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urls


@pytest.fixture(scope='function')
def driver():
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=opts)
    driver.get(urls.MAIN_URL)
    yield driver
    driver.quit()
