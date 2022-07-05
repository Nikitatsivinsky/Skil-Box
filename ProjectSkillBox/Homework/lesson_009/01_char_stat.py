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
from pprint import pprint


class FileAnalysis:

    __path_analysis_file = None
    __name_analysis_file = None
    file_to_read = None
    files_for_analysis_list = []
    letters_dict = {}

    def __init__(self, file_name):
        self.search_file(file_name)

    def get_file_path(self):
        return self.__path_analysis_file

    def get_file_name(self):
        return self.__name_analysis_file


    def search_file(self, file_name):
        for dirpath,dirnames,filenames in os.walk(os.path.dirname(__file__)):
            if file_name in filenames:
                print(f"Файл найден в директории {dirpath}")
                self.__path_analysis_file = os.path.join(dirpath, file_name)
                self.__name_analysis_file = file_name
                if self.get_file_path().endswith('.zip'):
                    print(f"Обнаружен: Zip Архив.")
                    self.z_files()

    def z_files(self):
        z_file = zfile.ZipFile(self.get_file_path(), 'r')
        for file_in_zip in z_file.namelist():
            print(f"В Zip Архиве обнаружен файл: {file_in_zip}")
            if file_in_zip.endswith('.txt'):
                file_operation_confirmation = input(f"Вы хотите расспаковать из Zip Архива текстовый файл: {file_in_zip} \n"
                                    f"Введите Yes/Y если Да\n"
                                    f"Найти другие текстовые файлы - Введите No/N\n"
                                    f"Ваш ввод: ")
                if file_operation_confirmation == 'Yes' or 'Y':
                    self.files_for_analysis_list.append(file_in_zip)
                    z_file.extract(file_in_zip)
                else:
                    continue

class AnalizedLinesInFile(FileAnalysis):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.initialization_lines_to_dict()

    def initialization_lines_to_dict(self):
        for founded_files in self.files_for_analysis_list:
            self.file_to_read = open(file=founded_files, mode='r', encoding='cp1251')
            for line in self.file_to_read.readlines():
                for letter in line:
                    if letter.isalpha():
                        if letter in self.letters_dict:
                            self.letters_dict[letter] += 1
                        else:
                            self.letters_dict[letter] = 1


class CounterLettersInFiles(AnalizedLinesInFile):
    def __init__(self, file_name):
        super().__init__(file_name)
        self.result_method()

    def result_method(self):
        flag_input_method = input(f'Если Вы хотите вывести результат на консоль - введите 1 \n'
                                  f'Если Вы хотите вывести результат в свой текстовый файл - введите 2\n'
                                  f'Ваш ввод:')

        letter_head, count_head, all_count_letter = 'Буква', 'Частота', 'Итого'
        head_discription = f'|{letter_head:^10}|{count_head:^10}|'
        head_line = f'{"+":-<11}{"+":-<11}{"+"}'

        if int(flag_input_method) == 1:
            print(head_line)
            print(head_discription)
            print(head_line)
            total_letter_counter = 0
            for letter, counter in self.letters_dict.items():
                print(f'|{letter:^10}|{counter:^10}|')
                total_letter_counter += counter
            print(head_line)
            print(f'|{all_count_letter:^10}|{total_letter_counter:^10}|')
            print(head_line)

        elif int(flag_input_method) == 2:
            name_result_file = input(f'Введите название файла')
            if name_result_file.endswith('.txt'):
                with open(name_result_file, mode='w+', encoding='utf-8') as file:
                    file.write(head_line)
                    file.write(head_discription)
                    file.write(head_line)
                    total_letter_counter = 0
                    for letter, counter in self.letters_dict.items():
                        file.write(f'|{letter:^10}|{counter:^10}|')
                        total_letter_counter += counter
                    file.write(head_line)
                    file.write(f'|{all_count_letter:^10}|{total_letter_counter:^10}|')
                    file.write(head_line)
                    print(f'Файл находиться по пути: {file.name}')






file = CounterLettersInFiles(file_name='voyna-i-mir.txt.zip')


















# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

