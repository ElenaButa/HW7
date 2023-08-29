import os.path
import zipfile
from zipfile import ZipFile

from conftest import tmp_path, resources_path

'''2. Создать новые тесты, которые заархивируют имеющиеся 
в resources различные типы файлов в один архив в tmp и 
проверят тестом в архиве каждый из файлов, что он является тем самым, 
который был заархивирован, не распаковывая архив.'''


def test_create_zip_files():
    files = os.listdir(resources_path)

    with ZipFile(os.path.join(tmp_path, 'resources_files.zip'), mode='w',
                 compression=zipfile.ZIP_DEFLATED) as filezip:
        for file in files:
            add_file = os.path.join(resources_path, file)
            filezip.write(add_file)

    assert os.path.exists(os.path.join(tmp_path, 'resources_files.zip'))


def test_read_zip_file():
    with ZipFile(os.path.join(tmp_path, 'resources_files.zip')) as filezip:
        names_files_zip = [os.path.basename(file) for file in filezip.namelist()]

        assert names_files_zip == os.listdir(resources_path)