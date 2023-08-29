import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selene import browser

tmp_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), 'tmp')
resources_path = os.path.join(os.path.dirname((os.path.abspath(__file__))), 'resources')

#вынесена настройка браузера в conftest (замечание "Необязательное-1")

@pytest.fixture()
def download_browser(scope='session', autouse=True):
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": tmp_path,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver

@pytest.fixture(scope='session', autouse=True)
def directory():
    place = os.listdir(tmp_path)
    #для удаления файла после теста
    for file in place:
        os.remove(os.path.join(tmp_path, file))
