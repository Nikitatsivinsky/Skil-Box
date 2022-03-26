# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
import random

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile (center_position, point_randome):
    color = sd.COLOR_YELLOW
    #Circle for Smile
    sd.circle(center_position=center_position, radius=70, width=6) #circle
    #Eye Right
    eye_r_position_x = point_randome[0] - 20 #eye right x
    eye_r_position_y = point_randome[1] + 20 #eye right y
    eye_r_position = sd.get_point(eye_r_position_x,eye_r_position_y) #eye right XY
    sd.circle(center_position=eye_r_position,color=color, radius=10, width=6)#eye right draw
    #Eye Left
    eye_l_position_x = point_randome[0] + 20 #eye left x
    eye_l_position_y = point_randome[1] + 20 #eye left y
    eye_l_position = sd.get_point(eye_l_position_x,eye_l_position_y) #eye left XY
    sd.circle(center_position=eye_l_position,color=color, radius=10, width=6)#eye left draw
    #Mouth 4 point coordinate
    point_mouth_1 = sd.get_point(point_randome[0] + 40, point_randome[1] - 10)
    point_mouth_2 = sd.get_point(point_randome[0] + 20, point_randome[1] - 25)
    point_mouth_3 = sd.get_point(point_randome[0] - 20, point_randome[1] - 25)
    point_mouth_4 = sd.get_point(point_randome[0] - 40, point_randome[1] - 10)
    point_list = []#open list for mouth
    point_list.extend([point_mouth_1,point_mouth_2,point_mouth_3,point_mouth_4])#point list for mouth
    sd.lines(point_list,closed=False,color=color, width=6) #paint mouth

for smile_draw in range (10): #How much Smiles Paint?
    random_point_x = random.randint(100, 500)#x for random position
    random_point_y = random.randint(100, 500)#y for random position
    point_list = [random_point_x, random_point_y]# Random position list for enother operation
    point = sd.get_point(random_point_x, random_point_y)# random position
    smile(center_position=point, point_randome=point_list)

sd.pause()