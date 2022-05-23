# -*- coding: utf-8 -*-

import simple_draw as sd
import snowfall

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)

N = 10

snowfall.make_snowfall_list(N)
print(snowfall.list_coordinates)
print(snowfall.length_snow)
print(snowfall.abc_list)

while True:
    snowfall.make_snowfall_background()
    snowfall.move_snowfall_in_list()
    snowfall.make_snowfall()
    snowfall.number += 1

    # if snowfall.list_coordinates[snowfall.number][1] >= snowfall.length_snow[snowfall.number]:
    #     snowfall.list_fallen()
    #     for i in range(len(snowfall.fallen_list)):
    #         point = sd.get_point(snowfall.fallen_list[i][0], snowfall.fallen_list[i][1])
    #         sd.snowflake(center=point, length=snowfall.snowflakes_fallen_lengths[i], color=sd.COLOR_WHITE,
    #                      factor_a=snowfall.abc_list[i][0],
    #                      factor_b=snowfall.abc_list[i][1],
    #                      factor_c=snowfall.abc_list[i][2]
    #                      )
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
