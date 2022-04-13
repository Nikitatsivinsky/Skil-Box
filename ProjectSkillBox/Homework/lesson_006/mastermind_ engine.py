import random

HIDDEN_NUMBER = int


def generated_hidden_number():
    global HIDDEN_NUMBER
    global number_list
    HIDDEN_NUMBER = random.randint(1000, 9999)
    number_list = list(str(HIDDEN_NUMBER))


def check_number(IMPORT_VALUE):
    global move_result
    print('import number ', IMPORT_VALUE)
    IMPORT_VALUE = list(str(IMPORT_VALUE))
    counter_cows = 0
    counter_bulls = 0
    for check_cows in IMPORT_VALUE:
        if check_cows in number_list:
            counter_cows += 1
    counter_function = 0
    for check_bulls in number_list:
        if check_bulls in IMPORT_VALUE[counter_function]:
            counter_bulls += 1
        counter_function += 1
    counter_cows -= counter_bulls

    print('Быков - ', counter_bulls)
    print('Коров -', counter_cows)
    move_result = {'bulls': counter_bulls, 'cows': counter_cows}


generated_hidden_number()
print('hiden number  ', HIDDEN_NUMBER)
check_number(IMPORT_VALUE= random.randint(1000, 9999))

