import simple_draw as sd


def sun():
    point = sd.get_point(230,800)
    line = sd.circle(center_position = point, radius=90, width=0)
    sd.vector(start=point, length=150,angle=0, color=sd.background_color)
    angle = 0
    counter_lines = 0
    while counter_lines < 361:
        sd.vector(start=point, length=180, angle=counter_lines, width=1)
        counter_lines += 20