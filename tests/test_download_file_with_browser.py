import time
import os
from conftest import * #убраны неиспользуемые импорты (замечание "Необязательное-2")


# TODO оформить в тест, добавить ассерты и использовать универсальный путь к tmp

def test_download_and_size_file_with_browser(download_browser):

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()

    time.sleep(5)

    #проверка, что файл размещен в папке (замечание 4)
    assert os.path.exists(os.path.join(tmp_path, 'pytest-main.zip'))

    #проверка размера файла (замечание 5)
    size = os.path.getsize(os.path.join(tmp_path, 'pytest-main.zip'))
    assert size == 1592483
