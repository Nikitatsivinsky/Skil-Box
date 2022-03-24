# -*- coding: utf-8 -*-

# (if/elif/else)

# По номеру месяца вывести кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

# Номер месяца получать от пользователя следующим образом
def user_input():
    while True:
        getNumber = input("Введите, пожалуйста, номер месяца: ")  # Ввод числа
        if getNumber.isdigit(): return getNumber

user_input = user_input()
month = int(user_input)
print('Вы ввели', month)
month_list = list(range(1, 13))
month_tuple = [30, 28, 30, 29, 30, 29, 29, 31, 30, 29, 28, 29]
month_tuple = dict(zip(month_list, month_tuple))
month_name = (
    'Январе', 'Феврале', 'Марте', 'Апреле', 'Майе', 'Июне', 'Июле',
    'Августе', 'Сентябре', 'Октябре', 'Ноябре', 'Декабре'
)
my_month = month_tuple.keys()
month_name_tuple = dict(zip(my_month, month_name))

if month > 12 or month < 1:
    print('Неверное число месяца')
elif month_name[month - 1] in month_name[month - 1]:
    print('В', (month_name_tuple[month]), (month_tuple[month]), 'дней')
else:
    raise SystemExit('Я не знаю что ты там ввел, но оно не пашет...')
