#!/usr/bin/env python3
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

import os
import zipfile as zfile


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
        for dirpath, dirnames, filenames in os.walk(os.path.dirname(__file__)):
            if file_name in filenames:
                print(f"Зпрашиваемый файл или архив найден в директории {dirpath}")
                self.__path_analysis_file = os.path.join(dirpath, file_name) #init
                self.__name_analysis_file = file_name #init
                if self.get_file_path().endswith('.zip'):
                    print(f"Запрашиваемый файл является Zip Архивом.")
                    self.unzip_files()
                else:
                    self.files_for_analysis_list.append(self.get_file_path())

    def unzip_files(self):
        z_file = zfile.ZipFile(self.get_file_path(), 'r')
        for file_in_zip in z_file.namelist():
            print(f"В Zip Архиве обнаружен файл: {file_in_zip}")
            if file_in_zip.endswith('.txt'):
                file_operation_confirmation = input(
                    f"Вы хотите расспаковать из Zip Архива текстовый файл: {file_in_zip} \n"
                    f"Введите Yes/Y если Да\n"
                    f"Найти другие текстовые файлы - Введите No/N\n"
                    f"Ваш ввод: ")
                if file_operation_confirmation == 'Yes' or 'Y':
                    self.files_for_analysis_list.append(file_in_zip)
                    z_file.extract(file_in_zip)
                else:
                    continue
            else:
                exit('Поиск по Zip архиву закончился успешно. \n'
                     'В Zip архиве, нет TXT файлов, либо нет нужного текстового файла.')


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


class SortDict(AnalizedLinesInFile):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.choice_sorting_method()

    def choice_sorting_method(self):
        flag_sorting_method = input(f'Если Вы хотите отсортировать результат по частоте по возрастанию -  введите 1\n'
                                    f'Если Вы хотите отсортировать результат по частоте по убыванию -  введите 2\n'
                                    f'Если Вы хотите отсортировать результат по алфавиту по возрастанию -  введите 3\n'
                                    f'Если Вы хотите отсортировать результат по алфавиту по убыванию -  введите 4\n'
                                    f'Ваш ввод:')

        if int(flag_sorting_method) == 1:
            self.sort_by_count()
        elif int(flag_sorting_method) == 2:
            self.sort_by_count(descending=True)
        elif int(flag_sorting_method) == 3:
            self.sort_by_letter()
        elif int(flag_sorting_method) == 4:
            self.sort_by_letter(descending=True)
        else:
            self.choice_sorting_method()

    def sort_by_count(self, descending=False):
        sorted_dict = {}
        sorted_keys = sorted(self.letters_dict, key=self.letters_dict.get, reverse=descending)
        for w in sorted_keys:
            sorted_dict[w] = self.letters_dict[w]
        self.letters_dict = sorted_dict

    def sort_by_letter(self, descending=False):
        letters_list_for_sorting = []
        letters_dict_for_sorting = {}
        for letter, counter in self.letters_dict.items():
            letters_list_for_sorting.extend(letter)
        letters_list_for_sorting.sort(reverse=descending)
        for letter in letters_list_for_sorting:
            letters_dict_for_sorting[letter] = self.letters_dict[letter]
        self.letters_dict = letters_dict_for_sorting




class CounterLettersInFiles(SortDict):

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
            if not name_result_file.endswith('.txt'):
                name_result_file = name_result_file + '.txt'
            with open(name_result_file, mode='w+', encoding='utf-8') as file:
                file.write(f'{head_line}\n')
                file.write(f'{head_discription}\n')
                file.write(f'{head_line}\n')
                total_letter_counter = 0
                for letter, counter in self.letters_dict.items():
                    file.write(f'|{letter:^10}|{counter:^10}|\n')
                    total_letter_counter += counter
                file.write(f'{head_line}\n')
                file.write(f'|{all_count_letter:^10}|{total_letter_counter:^10}|\n')
                file.write(f'{head_line}\n')
                print(f'Файл находиться по пути: {os.path.join(os.path.dirname(__file__), file.name)}')

        else:
            self.result_method()


file = CounterLettersInFiles(file_name='voyna-i-mir.txt.zip')


















# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

