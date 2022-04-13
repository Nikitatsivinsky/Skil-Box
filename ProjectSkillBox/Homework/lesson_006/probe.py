number_list = ['1', '3', '2', '4']
import_value = ['1', '2', '3', '4']
print(number_list)
print(import_value)

counter_cows = 0
counter_bulls = 0
for check_cows in import_value:
    if check_cows in number_list:
        counter_cows += 1
counter_function = 0
for check_bulls in number_list:
    if check_bulls in import_value[counter_function]:
        counter_bulls += 1
    counter_function += 1
counter_cows -= counter_bulls

print('Быков - ', counter_bulls)
print('Коров -', counter_cows)

