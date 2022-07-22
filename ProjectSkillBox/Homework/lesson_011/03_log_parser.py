# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:

# _____________________________________________________Итератор_________________________________________________________


# from datetime import datetime
#
#
# class LogParser:
#     log_entries_dict = {}
#
#     def __init__(self, name_parsing_file):
#         self.value = None
#         self.date = None
#         self.name_parsing_file = name_parsing_file
#         self.get_line()
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#
#         for line, value in self.log_entries_dict.items():
#             self.log_entries_dict.pop(line)
#
#             if self.log_entries_dict == {}:
#                 raise StopIteration
#
#             return line, value
#
#     def get_line(self):
#         with open(self.name_parsing_file, mode='r', ) as file:
#             for line in file:
#                 time_text = str(line[1:27])
#                 try:
#                     self.date = datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S.%f")
#                     self.date = self.date.strftime("%Y-%m-%d %H:%M")
#                     self.value = str(line[29:]).strip()
#                     self.make_log_entries_dict()
#                 except ValueError:
#                     continue
#
#     def is_not_ok(self):
#         if self.value == 'NOK':
#             return True
#
#     def make_log_entries_dict(self):
#         if self.is_not_ok():
#             if self.date in self.log_entries_dict:
#                 self.log_entries_dict[self.date] += 1
#             else:
#                 self.log_entries_dict[self.date] = 1
#
#
# grouped_events = LogParser('events.txt')
#
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')


# ______________________________________________________Генератор_______________________________________________________

from datetime import datetime

name_input_file = 'events.txt'


def get_line(name_parsing_file):
    def decorator_func(func):
        log_entries_dict = {}
        try:
            with open(name_parsing_file, mode='r', ) as file:
                for line_in_file in file:
                    try:
                        time_text = str(line_in_file[1:27])
                        date = datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S.%f")
                        date = date.strftime("%Y-%m-%d %H:%M")
                        value = str(line_in_file[29:]).strip()
                        func(value, date, log_entries_dict)
                    except ValueError as exc:
                        print(f'Ошибка в файле {name_input_file}, в строке: {line_in_file}'
                              f'Ошибка {type(exc).__name__}: {exc}\n'
                              f'Пропускаю строчку.\n')
                        pass

        finally:
            for return_line, value in log_entries_dict.items():
                yield f'[{return_line}] {value}'

    return decorator_func


@get_line(name_input_file)
def if_nok_in_line(value, date, log_entries_dict):
    if value == 'NOK':
        if date in log_entries_dict:
            log_entries_dict[date] += 1
        else:
            log_entries_dict[date] = 1


for line in if_nok_in_line:
    print(line)

#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
