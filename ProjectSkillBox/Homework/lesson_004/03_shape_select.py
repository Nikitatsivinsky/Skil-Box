# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

#Выбор фигуры
print('Выбирите фигуру из доступных!')
dict_figures = {'Треугольник': 1,
                 'Квадрат': 2,
                 'Пятиугольник': 3,
                 'Шестиугольник': 4}
for key,value in dict_figures.items():
	print(key, ':', value)
input_figure_number = int(input('Ваш номер фигуры: '))

# Условия прохождения фигуры
if input_figure_number > 4:
    print('Слишком большое число. Такой фигуры нет!')
    exit()
elif input_figure_number < 1:
    print('Слишком маленькое число число. Такой фигуры нет!')
    exit()

# Ввод цвета
print('Выбирите цвет фигур из доступных!')
print(' Красный - 1 \n Оранжевый - 2 \n Жёлтый -3 \n Зеленый - 4 \n Голубой - 5 \n Синий - 6 \n Фиолетовый - 7')
input_color = int(input('Ваш номер цвета:'))

# Условия ввода цвета
if input_color > 7:
    print('Слишком большое число. Такого цвета нет!')
    exit()
elif input_color < 1:
    print('Слишком маленькое число число. Такого цвета нет!')
    exit()
elif input_color == 1:
    input_color = sd.COLOR_RED
elif input_color == 2:
    input_color = sd.COLOR_ORANGE
elif input_color == 3:
    input_color = sd.COLOR_YELLOW
elif input_color == 4:
    input_color = sd.COLOR_GREEN
elif input_color == 5:
    input_color = sd.COLOR_CYAN
elif input_color == 6:
    input_color = sd.COLOR_BLUE
elif input_color == 7:
    input_color = sd.COLOR_PURPLE

# Функция отрисовки
def draw(point, length, range_cycle, angle_ualue,color):
    angle = 0
    for cycle in range(range_cycle):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        point = v1.end_point
        angle += angle_ualue
        sd.line(start_point=v1.start_point, end_point=v1.end_point, width=4, color=color)
        v1.draw()

# Функция треугольника
def triangle(point):
    length_triangle = 200
    point_triangle = point
    range_triangle = 3
    draw(point=point_triangle, length=length_triangle, range_cycle=range_triangle, angle_ualue=120,color=input_color)

# Функция квадрата
def square(point):
    length_square = 170
    point_square = point
    range_square = 4
    draw(point=point_square, length=length_square, range_cycle=range_square, angle_ualue=90, color=input_color)

# Функция пятиугольника
def pentagon(point):
    length_pentagon = 140
    point_pentagon = point
    range_pentagon = 5
    draw(point=point_pentagon, length=length_pentagon, range_cycle= range_pentagon, angle_ualue=72, color=input_color)

# Функция шестиугольника
def hexagon(point):
    length_hexagon = 120
    point_six_hexagon = point
    range_six_hexagon = 6
    draw(point=point_six_hexagon, length=length_hexagon, range_cycle=range_six_hexagon, angle_ualue=60,
         color=input_color)

# Функция выбора фигуры
if input_figure_number == 1:
    print('Понял! Заец Рисую твой треугольник!')
    triangle(point=sd.get_point(200, 200))
elif input_figure_number == 2:
    print('Понял! Заец Рисую твой квадрат!')
    square(point=sd.get_point(210, 200))
elif input_figure_number == 3:
    print('Понял! Заец Рисую твой пятиугольник!')
    pentagon(point=sd.get_point(230, 200))
else:
    print('Понял! Заец Рисую твой шестиугольник!')
    hexagon(point=sd.get_point(240, 200))

sd.pause()


