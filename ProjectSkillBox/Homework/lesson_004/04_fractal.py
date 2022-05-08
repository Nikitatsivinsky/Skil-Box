# -*- coding: utf-8 -*-

import simple_draw as sd
import random


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# sd.set_screen_size(width=1200, height=800)
#
# POINT_0 = sd.get_point(600, 30)
# ANGLE_DRAW = 90
# LENGTH_DRAW = 200
#
#
# def draw_branches(start_point, angle_draw, length_draw, delta=30):
#     if length_draw < 5:
#         return
#
#     vector = sd.get_vector(start_point=start_point, angle=angle_draw, length=length_draw, width=1)
#     vector.draw(width=1)
#     next_point = vector.end_point
#     next_angle_left = angle_draw - delta
#     next_angle_right = angle_draw + delta
#     next_length = length_draw * .75
#     draw_branches(start_point=next_point, angle_draw=next_angle_left, length_draw=next_length, delta=delta)
#     draw_branches(start_point=next_point, angle_draw=next_angle_right, length_draw=next_length, delta=delta)
#
# draw_branches(start_point=POINT_0, angle_draw=ANGLE_DRAW,length_draw=LENGTH_DRAW)





# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

sd.set_screen_size(width=1500, height=1000)

POINT_0 = sd.get_point(750, 30)
ANGLE_DRAW = 90
LENGTH_DRAW = 200


def draw_branches(start_point, angle_draw, length_draw, delta=30):
    if length_draw < 3:
        return

    vector = sd.get_vector(start_point=start_point, angle=angle_draw, length=length_draw, width=1)
    vector.draw(width=1)
    next_point = vector.end_point

    delta_random = random.randint(18,42)
    next_angle_left = angle_draw - delta_random
    next_angle_right = angle_draw + delta_random

    random_length = random.uniform(.6,0.9)
    next_length = length_draw * random_length


    draw_branches(start_point=next_point, angle_draw=next_angle_left, length_draw=next_length, delta=delta)
    draw_branches(start_point=next_point, angle_draw=next_angle_right, length_draw=next_length, delta=delta)


draw_branches(start_point=POINT_0, angle_draw=ANGLE_DRAW,length_draw=LENGTH_DRAW)


sd.pause()


