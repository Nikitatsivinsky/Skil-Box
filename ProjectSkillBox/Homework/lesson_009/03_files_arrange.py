# -*- coding: utf-8 -*-


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedir
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import os, datetime, zipfile
from pprint import pprint


class PosratName:

    __name = None
    filetime_dict = {}
    path_names_dict = {}

    def __init__(self, file_name):
        self.set_file_name(file_name)

    def set_file_name(self, file_name):
        self.__name = file_name

    def get_file_name(self):
        return self.__name

    def get_file_path(self):
        return os.path.dirname(__file__)


class ZipOperations(PosratName):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.copy_files_from_zip()
        self.read_file = None

    def zip_file(self):
        return zipfile.ZipFile(self.get_file_name(), mode='r')

    def filetime_initialization(self):
        with self.zip_file() as zf:
            for file in zf.infolist():
                date = datetime.datetime(*file.date_time)
                name = file.filename
                path = zipfile.Path(zf, name)
                if path.is_file():
                    self.filetime_dict[date] = (name, path.name)

    def copy_files_from_zip(self):

        with self.zip_file() as zf:
            for file in zf.infolist():
                path = zipfile.Path(zf, file.filename)
                if path.is_file():
                    date = datetime.datetime(*file.date_time)
                    output_dir = os.path.join(self.get_file_path(), str(date.year), str(date.month))
                    output_fname = os.path.join(output_dir, path.name)
                    if not os.path.exists(output_dir):
                        os.makedirs(output_dir)
                    # a = file_name
                    # a = 'icons2/icons/actions/address-book-new.png'
                    with open(output_fname, 'wb') as f:
                        f.write(path.read_bytes())


# import shutil
# import zipfile
#
# with zipfile.ZipFile('/path/to/my_file.apk') as z:
#     with z.open('/res/drawable/icon.png') as zf, open('temp/icon.png', 'wb') as f:
#         shutil.copyfileobj(zf, f)


# class OperationWithFiles(ZipOperations):
#
#     def __init__(self, file_name):
#         super().__init__(file_name)
#         path = None
#         self.folder_generation()

    # def folder_generation(self):
    #     self.path = os.path.join(self.get_file_path(), 'Result')
    #     if not os.path.exists(self.path):
    #         os.mkdir(self.path)
    #     for time, name_file in self.filetime_dict.items():
    #         year = time.strftime('%Y')
    #         month = time.strftime('%m')
    #         if os.path.exists(os.path.join(self.path, year)):
    #             pass
    #         else:
    #             os.mkdir(os.path.join(self.path, year))
    #         if os.path.exists(os.path.join(self.path, year, month)):
    #             pass
    #         else:
    #             os.mkdir(os.path.join(self.path, year, month))
    #         self.copy_files_from_zip(path_in_result=os.path.join(self.path, year, month), name_file=name_file)


file_name = ZipOperations('icons2.zip')


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
