# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем


def input_value():
    return input('Если хочешь что-нибудь сделать, сделай это сам: ')

def try_leeloo():
    global leeloo, input_data
    try:
        leeloo = int(input_data[4])
    except ValueError as exc:
        print(f'Невозможно преобразовать к числу введенные данные {input_data[4]}. Ошибка:{exc}')
        input_data = input_value()
        try_leeloo()
    except IndexError as exc:
        print(f'Выход за границы списка в введенных данных: {exc}')
        input_data = input_value()
        try_leeloo()
    except Exception as exc:
        print(f'Ошибка преобразования в строку: {exc}')
        input_data = input_value()
        try_leeloo()
    else:
        result = BRUCE_WILLIS * leeloo
        print(f"- Leeloo Dallas! Multi-pass № {result}!")

BRUCE_WILLIS = 42
leeloo = None

input_data = input_value()
try_leeloo()

# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение




