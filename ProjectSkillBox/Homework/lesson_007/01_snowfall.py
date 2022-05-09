# -*- coding: utf-8 -*-

import simple_draw as sd
import random

# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.N = 40
        self.list_coordinates = []
        self.length_snow = []
        self.abc_list = []
        self.fallen_list = []
        self.snowflakes_fallen_lengths = []
        self.abc_list_fallen = []
        self.point = 0
        self.point2 = 0

    def make_lists(self):
        for counter in range(self.N):
            self.list_coordinates.append([sd.random_number(100, 1200), sd.random_number(800, 1300)])
            self.length_snow.append(sd.random_number(20, 70))
            self.abc_list.append(
                [round(random.uniform(0.3, 1), 1), round(random.uniform(0.15, 0.55), 2), sd.random_number(50, 70)])

    def clear_previous_picture(self, i=0):
        point = sd.get_point(self.list_coordinates[i][0], self.list_coordinates[i][1])
        sd.start_drawing()
        sd.snowflake(center=point, length=self.length_snow[i], color=sd.background_color, factor_a=self.abc_list[i][0],
                     factor_b=self.abc_list[i][1], factor_c=self.abc_list[i][2])
        if self.list_coordinates[i][1] <= self.length_snow[i]:
            self.fallen_list.append([self.list_coordinates[i][0], self.list_coordinates[i][1]])
            self.snowflakes_fallen_lengths.append(self.length_snow[i])
            self.abc_list_fallen.append(
                [self.abc_list[i][0], self.abc_list[i][1], self.abc_list[i][2]])
            self.snowflakes_fallen_lengths.append(self.length_snow[i])

            self.list_coordinates.pop(i)
            self.length_snow.pop(i)
            self.abc_list.pop(i)


            self.length_snow.append(sd.random_number(20, 70))
            self.list_coordinates.append([sd.randint(0, 1200), 800 + 50])
            self.abc_list_fallen.append([round(random.uniform(0.3, 1), 1), round(random.uniform(0.15, 0.55), 2),
                                    sd.random_number(50, 70)])

        i += 1
        if i >= self.N:
            return


    def move(self, i=0):
        if self.list_coordinates[i][1] >= self.length_snow[i]:
            self.list_coordinates[i][1] -= sd.randint(20, 40)
            left_or_right_rand = sd.randint(0, 2)
            if left_or_right_rand < 0.5:
                self.list_coordinates[i][0] -= sd.randint(7, 10)
            else:
                self.list_coordinates[i][0] += sd.randint(7, 10)

            point2 = sd.get_point(self.list_coordinates[i][0], self.list_coordinates[i][1])
            sd.snowflake(center=point2, length=self.length_snow[i], color=sd.COLOR_WHITE, factor_a=self.abc_list[i][0],
                    factor_b=self.abc_list[i][1], factor_c=self.abc_list[i][2])
        i += 1
        if i >= self.N:
            return

    def can_fall(self):
        for i in range(len(self.fallen_list)):
            point = sd.get_point(self.fallen_list[i][0], self.fallen_list[i][1])
            sd.snowflake(center=point, length=self.snowflakes_fallen_lengths[i], color=sd.COLOR_WHITE,
                         factor_a=self.abc_list[i][0], factor_b=self.abc_list[i][1], factor_c=self.abc_list[i][2])




flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    # flake.draw(i=cycle)
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
