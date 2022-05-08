input_value = input()


def summa(result_sum=0):
    for i in input_value:
        result_sum += int(i)
    return result_sum


def product():
    result_product = 0
    value = []
    for i in [len(input_value)]:
        for i in input_value:
            value.extend(i)
        for i in range(len(input_value)):
            result_product = result_product * int(value[int(i)])
    return result_product


print('Сумма цифр = {}'.format(summa()))
print('Произведение цифр = {}'.format(product()))
