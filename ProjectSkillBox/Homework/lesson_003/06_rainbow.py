# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# x_start = 50
# x_finish = 350
# for color in rainbow_colors:
#     for rainbow in range (1):
#         start_point = sd.get_point(x_start, 50)
#         end_point = sd.get_point(x_finish, 450)
#         x_start += 5
#         x_finish += 5
#         sd.line(start_point, end_point,color, width=4)





# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
x_rainbow = 200
y_rainbow = -300
for color in rainbow_colors:
    for rainbow in range (1):
        radius = 600
        start_point = sd.get_point(x_rainbow, y_rainbow)
        x_rainbow += 10
        y_rainbow += 48
        sd.circle(center_position=start_point, radius=radius, color=color, width=50)

sd.pause()