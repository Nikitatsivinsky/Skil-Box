# -*- coding: utf-8 -*-

# Игра «Быки и коровы»
# https://goo.gl/Go2mb9
#
# Правила:
# Компьютер загадывает четырехзначное число, все цифры которого различны
# (первая цифра числа отлична от нуля). Игроку необходимо разгадать задуманное число.
# Игрок вводит четырехзначное число c неповторяющимися цифрами,
# компьютер сообщают о количестве «быков» и «коров» в названном числе
# «бык» — цифра есть в записи задуманного числа и стоит в той же позиции,
#       что и в задуманном числе
# «корова» — цифра есть в записи задуманного числа, но не стоит в той же позиции,
#       что и в задуманном числе
#
# Например, если задумано число 3275 и названо число 1234,
# получаем в названном числе одного «быка» и одну «корову».
# Очевидно, что число отгадано в том случае, если имеем 4 «быка».
#
# Формат ответа компьютера
# > быки - 1, коровы - 1


# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
#
# В текущем модуле (lesson_006/01_mastermind.py) реализовать логику работы с пользователем:
#   модуль движка загадывает число
#   в цикле, пока число не отгадано
#       у пользователя запрашивается вариант числа
#       модуль движка проверяет число и выдает быков/коров
#       результат быков/коров выводится на консоль
#  когда игрок угадал таки число - показать количество ходов и вопрос "Хотите еще партию?"
#
# При написании кода учитывайте, что движок игры никак не должен взаимодействовать с пользователем.
# Все общение с пользователем делать в текущем модуле. Представьте, что движок игры могут использовать
# разные клиенты - веб, чатбот, приложение, етс - они знают как спрашивать и отвечать пользователю.
# Движок игры реализует только саму функциональность игры.
# Это пример применения SOLID принципа (см https://goo.gl/GFMoaI) в архитектуре программ.
# Точнее, в этом случае важен принцип единственной ответственности - https://goo.gl/rYb3hT

from termcolor import cprint, colored
from mastermind_engine import make_number, check_the_number

user_number = '0'


def input_and_verify_user_number():
    while True:
        global user_number
        user_number = input('Введите Ваше число: ')
        if not user_number.isdigit():
            print('Вы ввели неверные символы, вводите только цифры!')
        elif user_number[0] == '0':
            print('Первое введеное число равно нулю, такого быть не должно, введите число, '
                  'которое начинается с другой цифры!')
        elif len(user_number) != 4:
            print('Вы ввели неверное количество символов, введите 4 цифры!')
        elif len(set(user_number)) != 4:
            print('Вы ввели повторяющиеся числа, введите заново значение с неповторяющимися цифрами!')
        else:
            break


if __name__ == '__main__':
    count_of_iteration = 1
    make_number()
    while True:
        input_and_verify_user_number()
        bulls_and_cows = check_the_number(user_number)
        cprint(f"быки - {bulls_and_cows['bulls']}, коровы - {bulls_and_cows['cows']}", color='red')
        if bulls_and_cows['bulls'] == 4:
            cprint(f'Вы угадали число {user_number} за {count_of_iteration} ходов!!!', color='magenta')
            _user_questions = str(input(colored('Хотите сыграть еще партию?(yes/no): ', color='blue')))
            if _user_questions == 'yes':
                count_of_iteration = 1
                make_number()
                continue
            else:
                break
        count_of_iteration += 1
    cprint('Спасибо, что играли в нашу игру!!!', color='cyan')

# зачет!
