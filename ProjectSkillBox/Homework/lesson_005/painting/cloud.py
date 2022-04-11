import simple_draw as sd


def cloud():
    x = sd.randint(850, 950)
    y = sd.randint(750, 850)
    for clouds in range(3):
        radius = sd.randint(30, 50)
        point = sd.get_point(x, y)
        if clouds == 1:
            radius = 60
            sd.circle(center_position=point, radius=radius, color=sd.COLOR_WHITE, width=0)
            x -= 60
            continue
        sd.circle(center_position=point, radius=radius, color=sd.COLOR_WHITE, width=0)
        x -= 60
    x = 230
    for clouds_sun in range(3):
        radius = sd.randint(30, 50)
        cloud = sd.get_point(x, 730)
        if clouds_sun == 1:
            radius = 50
            sd.circle(center_position=cloud, radius=radius, color=sd.COLOR_WHITE, width=0)
            x += 60
            continue
        sd.circle(center_position=cloud, radius=radius, color=sd.COLOR_WHITE, width=0)
        x += 60
    x = 430
    for clouds_sun in range(3):
        radius = sd.randint(40, 50)
        cloud = sd.get_point(x, 630)
        if clouds_sun == 1:
            radius = 65
            sd.circle(center_position=cloud, radius=radius, color=sd.COLOR_WHITE, width=0)
            x += 60
            continue
        sd.circle(center_position=cloud, radius=radius, color=sd.COLOR_WHITE, width=0)
        x += 60

