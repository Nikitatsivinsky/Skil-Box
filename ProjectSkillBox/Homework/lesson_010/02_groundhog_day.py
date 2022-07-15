# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint, choice


class CustomException(Exception):
    def __str__(self):
        return self.args[0]

class IamGodError(CustomException):
    pass


class DrunkError(CustomException):
    def __str__(self):
        return self.args[0] + ' Бутылок - ' + str(self.args[1])


class CarCrashError(CustomException):
    def __str__(self):
        return self.args[0] + ' Марка машины была - ' + str(self.args[1])


class GluttonyError(CustomException):
    pass


class DepressionError(CustomException):
    pass


class SuicideError(CustomException):
    pass


def one_day():
    random_number = randint(1, 13 * 6)
    model_car_list = ["Mazda", "Toyota", "Zaporogec"]
    list_exceptions = (IamGodError('Орк решил шо он бог и отьехал от гранаты!'),
                       DrunkError('Орк стырил пузырь паленой водяры и здох от отравления.', randint(3, 8)),
                       CarCrashError('Орк сел в машину и влетел в столб... Какая смешная смерть...',
                                     choice(model_car_list)),
                       GluttonyError('Орк сьел батончик с глютеном и умер от аллергии.'),
                       DepressionError('Орк здох от дипрессиии. Даже психотеропевт Джевелин не помог.'),
                       SuicideError('Орк наконец-то сам застрелился.'))

    if random_number % 13 == 0:
        raise list_exceptions[(random_number // 13) - 1]

    return randint(1, 7)


ENLIGHTENMENT_CARMA_LEVEL = 777
carma_counter = 0

while carma_counter < ENLIGHTENMENT_CARMA_LEVEL:
    try:
        carma_counter += one_day()
    except CarCrashError as exc:
        print(exc)
        print(exc.args[1] + ' отправилась в утиль')
    except CustomException as exc:
        print(exc)









# https://goo.gl/JnsDqu
