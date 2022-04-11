import simple_draw as sd


def human(x_human, y_human, width=3, radius=50):
    # Circle for Smile
    point = sd.get_point(x_human, y_human)
    sd.circle(center_position=point, radius=radius, width=width)
    # Eye Right
    eye_r_position_x = x_human - 20 #eye right x
    eye_r_position_y = y_human + 17 #eye right y
    eye_r_position = sd.get_point(eye_r_position_x, eye_r_position_y) #eye right XY
    sd.circle(center_position=eye_r_position, radius=(radius/100)*15, width=width)#eye right draw
    # Eye Left
    eye_l_position_x = x_human + 20 #eye left x
    eye_l_position_y = y_human + 17 #eye left y
    eye_l_position = sd.get_point(eye_l_position_x,eye_l_position_y) #eye left XY
    sd.circle(center_position=eye_l_position,radius=(radius/100)*15, width=width)#eye left draw
    # Mouth 4 point coordinate
    point_mouth_1 = sd.get_point(x_human + 30, y_human - 10)
    point_mouth_2 = sd.get_point(x_human + 20, y_human - 25)
    point_mouth_3 = sd.get_point(x_human - 20, y_human - 25)
    point_mouth_4 = sd.get_point(x_human - 30, y_human - 10)
    point_list = []#open list for mouth
    point_list.extend([point_mouth_1,point_mouth_2,point_mouth_3,point_mouth_4])#point list for mouth
    sd.lines(point_list, width=width) #paint mouth
    # Nose
    sd.vector(start=point, length=5, width=width, angle=90)
    # Body
    point_body = sd.get_point(x_human, y_human-radius)
    body = sd.vector(start=point_body, length=95, width=width, angle=270,)
    hand1 = sd.vector(start=sd.get_point(x_human, y_human-80), length=50, width=width, angle=310)
    hand2 = sd.vector(start=sd.get_point(x_human, y_human-80), length=50, width=width, angle=230)
    leg1 = sd.vector(start=sd.get_point(x_human, y_human-143), length=50, width=width, angle=315)
    leg2 = sd.vector(start=sd.get_point(x_human, y_human-143), length=50, width=width, angle=225)
