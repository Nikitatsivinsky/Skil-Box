# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers
#
# for i in get_prime_numbers(10000):
#     print(i)

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


# class PrimeNumbers:
#
#     def __init__(self, count):
#
#         self.count = count
#         self.prime_numbers = self.get_prime_numbers()
#
#     def __iter__(self):
#         self.i = -1
#         return self
#
#     def __next__(self):
#         try:
#             self.i += 1
#             return self.prime_numbers[self.i]
#         except IndexError:
#             raise StopIteration
#
#     def get_prime_numbers(self):
#         prime_numbers = []
#         for number in range(2, self.count+1):
#             for prime in prime_numbers:
#                 if number % prime == 0:
#                     break
#             else:
#                 prime_numbers.append(number)
#         return prime_numbers
#
#
#
# prime_number_iterator = PrimeNumbers(count=10000)
# for number in prime_number_iterator:
#     print(number)


# TODO после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#     return
#
# for number in get_prime_numbers(n=10000):
#     print(number)

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.

def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n+1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)

            yield number, is_lucky(number), is_palindromic(number)
    return

def is_lucky(number):

    list_number = []
    first_part = 0
    second_part = 0
    counter = 0

    for number in str(number):
        list_number.append(number)

    if len(list_number) == 1:
        return False

    if len(list_number) % 2 == 0:
        for i in range(0, len(list_number)):
            if counter == len(list_number) / 2:
                first_part += int(list_number[i])
            else:
                counter += 1
                second_part += int(list_number[i])
        if first_part == second_part:
            return True
        else:
            return False
    else:
        for i in range(0, len(list_number)):
            if not counter > round(len(list_number) / 2) - 1:
                counter += 1
                first_part += int(list_number[i])
            elif counter == round((len(list_number) / 2)):
                counter += 1
                continue
            else:
                counter += 1
                second_part += int(list_number[i])
        if first_part == second_part:
            return True
        else:
            return False

def is_palindromic(number):

    list_number = []

    for number in str(number):
        list_number.append(number)

    if len(list_number) == 1:
        return False

    for i in range(0, round((len(list_number) / 2))):
        if len(list_number) % 2 == 0:
            list_number_reverse = list_number[::-1]
            if list_number == list_number_reverse:
                return True
            else:
                return False
        else:
            list_number_reverse = list_number[::-1]
            center_number = list_number_reverse[round((len(list_number) / 2))]
            list_number.remove(center_number)
            list_number_reverse.remove(center_number)
            if list_number == list_number_reverse:
                return True
            else:

                return False



for number, is_lucky_num, is_palindromic_num in get_prime_numbers(n=10000):
    if is_lucky_num and is_palindromic_num:
        print(f'Число {number} счастливое и палиндромное')
    elif is_lucky_num:
        print(f'Число {number} счастливое')
    elif is_palindromic_num:
        print(f'Число {number} палиндромное')
    else:
        print(f'Число {number} обычное')