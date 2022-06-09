# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

import os
import zipfile as zfile

class Import:

    def __init__(self, file_name):

        self.file_name = file_name

        if self.file_name.endswith('.zip'):
            print(f"Обнаружен: Zip Архив.")
            self.z_files(file_name)
            file_name = os.path.join(os.path.dirname(__file__), self.file_name)

        self.Open_File(file_name)

    def Open_File(self, file_name):
        file = open(self.file_name, 'r')
        file.encode('utf8')
        for line in file:
            print(line)

        # file = open(file=file_name, mode='r', encoding="cp1251")
        # for line in file:
        #     print(line)

    def z_files(self, file_name):
        z_file = zfile.ZipFile(file_name, 'r')
        for filename in z_file.namelist():
            print(f"Обнаружен в Zip Архиве файл: {filename}")
            if filename.endswith('.txt'):
                print(f"Расспаковка из Zip Архива текстового файла: {filename}")
                file_name = filename
                z_file.extract(file_name)
        return file_name


class Number_Operation:
    pass

class Print_Result:
    pass




voyna_i_mir = Import(file_name='/home/niki/PycharmProjects/Skil-Box2/ProjectSkillBox/'
                               'Homework/lesson_009/python_snippets/voyna-i-mir.txt.zip')

















# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

