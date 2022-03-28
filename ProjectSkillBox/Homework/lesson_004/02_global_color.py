# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# Ввод цвета
print('Выбирите цвет фигур из доступных!')
print(' Красный - 1 \n Оранжевый - 2 \n Жёлтый -3 \n Зеленый - 4 \n Голубой - 5 \n Синий - 6 \n Фиолетовый - 7')
input_color = int(input('Ваш номер цвета:'))
# Условия цвета
if input_color > 7:
    print('Слишком большое число. Такого цвета нет!')
elif input_color < 1:
    print('Слишком маленькое число число. Такого цвета нет!')
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
else:
    print('Не знаю как у тебя получилось все сломать... Наверное ты БОГ! Попробуй ещё раз...')

# Фиункция отрисовки
def draw(point, length, range_cycle, angle_ualue,color):
    angle = 0
    for cycle in range(range_cycle):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
        point = v1.end_point
        angle += angle_ualue
        sd.line(start_point=v1.start_point, end_point=v1.end_point, width=4, color=color)
        v1.draw()

# треугольник
length_triangle = 200
point_triangle = sd.get_point(50, 400)
range_triangle = 3
start_point = point_triangle
draw(point=point_triangle, length=length_triangle, range_cycle=range_triangle, angle_ualue=120,color=input_color)

# квадрат
length_square = 170
point_square = sd.get_point(330, 400)
range_square = 4
draw(point=point_square, length=length_square, range_cycle=range_square, angle_ualue=90, color=input_color)

# пятиугольник
length_pentagon = 140
point_pentagon = sd.get_point(90, 100)
range_pentagon = 5
draw(point=point_pentagon, length=length_pentagon, range_cycle= range_pentagon, angle_ualue=72, color=input_color)

# шестиугольник
length_hexagon = 120
point_six_hexagon = sd.get_point(380, 100)
range_six_hexagon = 6
draw(point=point_six_hexagon, length=length_hexagon, range_cycle= range_six_hexagon, angle_ualue=60, color=input_color)

sd.pause()
