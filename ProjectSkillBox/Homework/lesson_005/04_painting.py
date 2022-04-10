# -*- coding: utf-8 -*-

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.


import simple_draw as sd
import painting.house as house
import painting.rainbow as rainbow
import painting.sun as sun
import painting.snowflakes as snow
import  painting.tree as tree


sd.set_screen_size(width=1800, height=1000)

#земля
point1_rectangle = sd.get_point(0,0)
point2_rectangle = sd.get_point(1800, 20)
sd.rectangle(left_bottom=point1_rectangle, right_top= point2_rectangle,color=sd.COLOR_GREEN)



width_home = 2
house.home(width_home)

rainbow.rainbow()

sun.sun()

snow.snow()

#TREE
point = sd.get_point(1700, 10)
length_draw = 150
delta=20
tree.tree(start_point=point, angle_draw=90, length_draw=length_draw, delta=delta)
point = sd.get_point(1500, 10)
length_draw = 70
delta=40
tree.tree(start_point=point, angle_draw=90, length_draw=length_draw, delta=delta)










sd.pause()