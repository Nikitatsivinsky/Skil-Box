import simple_draw as sd
import random

POINT_0 = sd.get_point(750, 30)
ANGLE_DRAW = 90
LENGTH_DRAW = 200


def tree(start_point, angle_draw, length_draw, delta=10):
    if length_draw < 10:
        return

    vector = sd.get_vector(start_point=start_point, angle=angle_draw, length=length_draw, width=1)
    vector.draw(width=1)
    next_point = vector.end_point

    delta_random = random.randint(18,30)
    next_angle_left = angle_draw - delta_random
    next_angle_right = angle_draw + delta_random

    random_length = random.uniform(.6,0.9)
    next_length = length_draw * random_length


    tree(start_point=next_point, angle_draw=next_angle_left, length_draw=next_length, delta=delta)
    tree(start_point=next_point, angle_draw=next_angle_right, length_draw=next_length, delta=delta)
