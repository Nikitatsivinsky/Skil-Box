# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger

from my_burger.bread import bread_top, bread_bottom
from my_burger.meat import meat_enter
from my_burger.cucumber import cucember_enter
from my_burger.tomato import tomato_enter
from my_burger.mayonnaise import mayonnaise_enter
from my_burger.chese import chese_enter
from my_burger.salat import salat_enter


print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n')
print(f'Создадим гамбургер!'
      f' В начале возьмем {bread_bottom},'
      f' на нё намажем {mayonnaise_enter}'
      f' и сверху добавим {salat_enter}. \n'
      f'Далее возьмем немного {tomato_enter} и {cucember_enter}, чтобы немного освежить наш гамбургер.'
      f' Подходим к финалу!  \nДобовляем нашу свежую {meat_enter} '
      f' и пока она горячая, добовляем {chese_enter}. Ждем пока он расплавиться! \n'
      f'Сверху кладем {bread_top}! И фиксируем все шпажкой!'
      f' Приятного аппетита! \n')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')



