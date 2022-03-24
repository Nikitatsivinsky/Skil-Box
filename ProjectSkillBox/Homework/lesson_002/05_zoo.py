#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pprint import pprint
# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1, 'bear')
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
#  и выведите список на консоль
# TODO здесь ваш код
print(zoo)
# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')
print(zoo)


# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

pprint(zoo[0] + ' сидит в клетке под номером ' +str((int(zoo.index('lion'))+1)) + ' a ' + zoo[6] + ' сидит в клетке под номером ' + str((int(zoo.index('lark'))+1)) )
# TODO здесь ваш код


