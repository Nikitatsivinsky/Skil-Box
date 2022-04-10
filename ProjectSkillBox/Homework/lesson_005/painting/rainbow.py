import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

def rainbow():
    x_rainbow = 300
    y_rainbow = -700
    for color in rainbow_colors:
        for rainbow in range (1):
            radius = 2000
            start_point = sd.get_point(x_rainbow, y_rainbow)
            x_rainbow += 10
            y_rainbow += 48
            sd.circle(center_position=start_point, radius=radius, color=color, width=50)
