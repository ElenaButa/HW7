from pypdf import PdfReader
from conftest import resources_path
import os.path

# TODO оформить в тест, добавить ассерты и использовать универсальный путь


def test_pdf_file():
    reader = PdfReader(os.path.join(resources_path, 'docs-pytest-org-en-latest.pdf'))
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert 'holger krekel' in page.extract_text()
    assert number_of_pages == 412

