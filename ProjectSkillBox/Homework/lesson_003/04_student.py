# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
plus_proc = 0
expenses_2 = expenses
month = 1
total_cash_2 = 0
first_month = expenses_2 - educational_grant
print('За ', month, ' месяц, - ', first_month, ' процентов.')
while month < 10:
    month += 1 #плюс месяц
    plus_proc = int((expenses_2/100)*3)
    expenses_2 += int(plus_proc)
    total_cash_2 += int(expenses_2-10000)
    print('За ', month, ' месяц, - ', expenses_2-10000, ' процентов.')

print('Студенту надо попросить ', total_cash_2+first_month,' рублей')

