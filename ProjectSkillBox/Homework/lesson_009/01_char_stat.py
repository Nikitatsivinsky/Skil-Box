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


    def Open_File(self):
        file = open(file=self.file_name, mode='r', encoding='cp1251')
        number_operation = Number_Operation(file_name=file)
        number_operation.collect()

    def z_files(self, file_name):
        if self.file_name.endswith('.zip'):
            print(f"Обнаружен: Zip Архив.")
        self.z_files(file_name)
        file_name = os.path.join(os.path.dirname(__file__), self.file_name)
        z_file = zfile.ZipFile(file_name, 'r')
        for filename in z_file.namelist():
            print(f"Обнаружен в Zip Архиве файл: {filename}")
            if filename.endswith('.txt'):
                print(f"Расспаковка из Zip Архива текстового файла: {filename}")
                file_name = filename
                z_file.extract(file_name)
                self.file_name = filename
        return file_name


class Number_Operation (Import):

    def __init__(self, file_name):
        self.analize_count = 4
        self.file = file_name
        self.stat = {}

    def collect(self): #Гениратор самих строчек
        self.sequence = ' ' * self.analize_count
        with self.file as file_line:
            # for line in file_line:
            #     self._collect_for_line(line=line[:-1])

    def _collect_for_line(self, line): #Строчки Лев Николаевич Толстой по буквам
        # for char in line:
        #     if char
        pass
















    # def prepare(self):
    #     self.totals = {}
    #     self.stat_for_generate = {}
    #     for sequence, char_stat in self.stat.items():
    #         self.totals[sequence] = 0
    #         self.stat_for_generate[sequence] = []
    #         for char, count in char_stat.items():
    #             self.totals[sequence] += count
    #             self.stat_for_generate[sequence].append([count, char])
    #             self.stat_for_generate[sequence].sort(reverse=True)
    #     print(f"self.totals = {self.totals}")
    #     # print(f"self.stat_for_generate = {self.stat_for_generate}")
    #     # print(f"self.stat IN PREPARE = {self.stat}")














class Print_Result (Import):
    pass




file = Import(file_name='/home/niki/PycharmProjects/Skil-Box2/ProjectSkillBox/'
                               'Homework/lesson_009/python_snippets/voyna-i-mir.txt.zip')
file.Open_File()


















# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

