import random

HIDDEN_NUMBER = int
move_result = tuple


def generated_hidden_number():
    global HIDDEN_NUMBER
    global number_list
    HIDDEN_NUMBER = random.randint(1000, 9999)
    number_list = list(str(HIDDEN_NUMBER))


def check_number(IMPORT_VALUE):
    global move_result
    check_cows_list = list(str(HIDDEN_NUMBER))
    IMPORT_VALUE = list(str(IMPORT_VALUE))
    counter_cows = 0
    counter_bulls = 0
    for check_cows in IMPORT_VALUE:
        if check_cows in check_cows_list:
            check_cows_list.remove(check_cows)
            counter_cows += 1
    counter_function = 0
    for check_bulls in number_list:
        if check_bulls in IMPORT_VALUE[counter_function]:
            counter_bulls += 1
        counter_function += 1
    counter_cows -= counter_bulls
    move_result = {'bulls': counter_bulls, 'cows': counter_cows}
    if counter_bulls == len(IMPORT_VALUE):
        print('Поздравляем! Вы угадали все числа!')
        again = True
        return again
    return move_result

