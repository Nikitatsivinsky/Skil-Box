# -*- coding: utf-8 -*-

# Создать модуль my_burger_packet. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger_packet и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger_packet

# ИМПОРТ ПАКЕТОВ
from my_burger_packet.bread import bread_top, bread_bottom
from my_burger_packet.meat import meat_enter
from my_burger_packet.cucumber import cucember_enter
from my_burger_packet.tomato import tomato_enter
from my_burger_packet.mayonnaise import mayonnaise_enter
from my_burger_packet.chese import chese_enter
from my_burger_packet.salat import salat_enter
########################################################
# ИМПОРТ МОДУЛЕЙ
import my_burger

print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> \n')
print(f'Создадим чизбургер!'
      f' В начале возьмем {bread_bottom},'
      f' на нё намажем {mayonnaise_enter}'
      f' и сверху добавим {salat_enter}. \n'
      f'Далее возьмем немного {tomato_enter} и {cucember_enter}, чтобы немного освежить наш гамбургер.'
      f' Подходим к финалу!  \nДобовляем нашу свежую {meat_enter} '
      f' и пока она горячая, добовляем {chese_enter}. Ждем пока он расплавиться! \n'
      f'Сверху кладем {bread_top}! И фиксируем все шпажкой!'
      f' Приятного аппетита! \n')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

my_burger.bread_top_module()
my_burger.mayonnaise_module()
my_burger.salat_module()
my_burger.tomato_module()
my_burger.cucember_module()
my_burger.meat_module()
my_burger.chese_module()
my_burger.bread_bottom_module()

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')


