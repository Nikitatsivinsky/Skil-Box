# -*- coding: utf-8 -*-

# (цикл for)
import random

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_point = sd.get_point(50,50)
end_point = sd.get_point(350,450)
def rainbow(point,step):
    sd.line(start_point, end_point, width=4)

for rainbow in range (100,100,10):
    bubble(point=point, step=5)

# for line in range (7):
#     color = rainbow_colors[line]
#     sd.line(start_point, end_point, color = color, width=4)
#     point = sd.random_point()
#     step = 5
#     bubble(point=point, step=step)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# TODO здесь ваш код

sd.pause()