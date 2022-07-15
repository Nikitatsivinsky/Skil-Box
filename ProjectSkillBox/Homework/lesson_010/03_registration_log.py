# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

from pprint import pprint


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def bad_line_write(line_input_file):
    with open('registrations_bad.log', 'a') as bad:
        bad.write(line_input_file)


with open('registrations.txt', 'r') as input_file:
    for line_input_file in input_file:
        try:
            name, mail, year = line_input_file[:-1].split(' ')
        except ValueError as exc:
            bad_line_write(f'"{line_input_file[:-1]}"Ошибка:  {exc.args[0]}')
            print(f'Ошибка, не все поля заполненны.Парметры: {exc.args[0]} \n')
            continue

        try:
            if not name.isalpha():
                raise NotNameError(' Поле имени содержит не только буквы')
            elif not '@' and '.' in mail:
                raise NotEmailError(' Некорректное поле емейл')
            elif not 10 < int(year) < 100:
                raise ValueError(' Некорректный возраст, дебил.')
            else:
                with open('registrations_good.log', 'a') as good:
                    good.write(line_input_file)
        except NotNameError as exc:
            bad_line_write(f'"{line_input_file[:-1]}"Парметры:  {exc.args[0]} \n')
        except NotEmailError as exc:
            bad_line_write(f'"{line_input_file[:-1]}"Парметры:  {exc.args[0]} \n')
        except ValueError as exc:
            bad_line_write(f' "{line_input_file[:-1]}" Парметры:  {exc.args[0]} \n')
        except Exception as exc:
            bad_line_write(f'В строке "{line_input_file[:-1]}" Трабла: {exc.args[0]}\n')
