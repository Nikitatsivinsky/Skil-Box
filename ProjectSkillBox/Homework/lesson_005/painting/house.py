
import simple_draw as sd

def home(width=1):
    start_point = sd.get_point(500,100)
    house_draw = sd.get_vector(start_point=start_point, length=250, angle=0, width=width)
    house_draw.draw()
    angel = 0
    for i in range(3):
        point = house_draw.end_point
        angel += 90
        house_draw = sd.get_vector(start_point=point, length=250, angle=angel,width=width)
        house_draw.draw()
        if angel == 270:
            point = sd.get_point(500, 350)
            angel = 45
            roof_paint = sd.get_vector(start_point=point, length=178, angle=45,width=width)
            roof_paint.draw()
            angel -= 90
            roof_paint = sd.get_vector(start_point=roof_paint.end_point, length=178, angle=angel,width=width)
            roof_paint.draw()
            continue

    start_point = sd.get_point(575,150)
    window_draw = sd.get_vector(start_point=start_point, length=100, angle=0, width=width)
    window_draw.draw()
    window_draw = sd.get_vector(start_point=window_draw.end_point, length=150, angle=90, width=width)
    window_draw.draw()
    window_draw = sd.get_vector(start_point=window_draw.end_point, length=100, angle=180, width=width)
    window_draw.draw()
    window_draw = sd.get_vector(start_point=window_draw.end_point, length=150, angle=270, width=width)
    window_draw.draw()

    start_point = sd.get_point(575,225)
    window_draw = sd.get_vector(start_point=start_point, length=100, angle=0, width=width)
    window_draw.draw()

    start_point = sd.get_point(625, 150)
    window_draw = sd.get_vector(start_point=start_point, length=150, angle=90, width=width)
    window_draw.draw()









