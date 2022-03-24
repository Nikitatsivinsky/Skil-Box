# Программа созданна для автоматического подсчета строк.
# К примеру: У вас есть список из 5 програм которые нужно скачать, вы скачали 3 и 4ю, Вам нужно узнать сколько осталось,
# и какие это программы. Вводите число 5, потом 3,4 и 0 - завершение ввода.


all_strings = int(input('Введите сколько всего строк: '))
while all_strings < 1:
    print('Ошибка: Число не может иметь отрицательное значение или равняться нулю!')
    all_strings = int(input('Заново введите сколько всего строк: '))
input_string_list = []
input_string = int(input('Введите номер строчки которая уже есть в списке: '))
if input_string < int(1):
    print('Ошибка: Число не может иметь отрицательное значение!')
if all_strings < input_string:
    print('Ошибка: Число больше чем всего количество строк!')

while input_string != int(0):
    input_string_list.append(input_string)
    input_string = int(input('Введите номер строчки которая уже есть в списке, либо 0 - завершение ввода: '))
    if input_string < int(0):
        print('Ошибка: Число не может иметь отрицательное значение!')
        if all_strings < input_string:
           print('Ошибка: Число больше чем количество строк!')

all_strings = list(range(1, (all_strings + 1)))
all_strings_2 = set(all_strings)
input_string_list_2 = set(input_string_list)

if all_strings_2 == input_string_list_2:
    print('Все Ваши строки есть в списке!')
elif input_string_list_2 > all_strings_2:
    print('Вы ввели слишком много строк! Их больше чем у Вас есть изначально!')

else:
    print('В список не входят строки : ' + str(set(all_strings) - set(input_string_list))[1:-1])
