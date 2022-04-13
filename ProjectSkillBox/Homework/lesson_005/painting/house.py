
import simple_draw as sd



def home(width=1):
    fist_point = sd.get_point(500, 20)
    second_point = sd.get_point(1000,340)
    sd.rectangle(left_bottom=fist_point, right_top=second_point, color=sd.COLOR_ORANGE, width=0)
    # Оконтовка
    sd.rectangle(left_bottom=fist_point, right_top=second_point, color=sd.COLOR_DARK_ORANGE, width=3)
    # Кирпичи
    next_line_y = 0
    for bricks_line in range (1):
        for bricks in range (8):
            x_fistpoint_brick = 500
            y_fistpoint_brick = 20 + next_line_y
            x_secondpoint_brick = 550
            y_secondpoint_brick = 40 + next_line_y
            for brick_fist in range(10):
                fist_point = sd.get_point(x_fistpoint_brick, y_fistpoint_brick)
                second_point = sd.get_point(x_secondpoint_brick, y_secondpoint_brick)
                sd.rectangle(left_bottom=fist_point, right_top=second_point, color=sd.COLOR_DARK_ORANGE, width=3)
                x_fistpoint_brick += 50
                x_secondpoint_brick += 50
            x_fistpoint_brick_second = 525
            y_fistpoint_brick_second = 40 + next_line_y
            x_secondpoint_brick_second = 575
            y_secondpoint_brick_second = 60 + next_line_y
            for brick_second in range(9):
                fist_point = sd.get_point(x_fistpoint_brick_second, y_fistpoint_brick_second)
                second_point = sd.get_point(x_secondpoint_brick_second, y_secondpoint_brick_second)
                sd.rectangle(left_bottom=fist_point, right_top=second_point, color=sd.COLOR_DARK_ORANGE, width=3)
                x_fistpoint_brick_second += 50
                x_secondpoint_brick_second += 50

            next_line_y += 40
    #Окно
    fist_point_window = sd.get_point(675, 81)
    second_point_window = sd.get_point(825,260)
    sd.rectangle(left_bottom=fist_point_window, right_top=second_point_window, color=sd.COLOR_CYAN, width=0)
    sd.rectangle(left_bottom=fist_point_window, right_top=second_point_window, color=sd.COLOR_DARK_ORANGE, width=6)
    fist_point_window = sd.get_point(750, 81)
    second_point_window = sd.get_point(750,260)
    sd.line(start_point=fist_point_window,end_point=second_point_window, color=sd.COLOR_DARK_ORANGE,width=6)
    fist_point_window = sd.get_point(675, 190)
    second_point_window = sd.get_point(825, 190)
    sd.line(start_point=fist_point_window, end_point=second_point_window, color=sd.COLOR_DARK_ORANGE, width=6)
    #Крыша
    fist_point_window = sd.get_point(450, 340)
    second_point_window = sd.get_point(1050, 340)
    therd_point_window = sd.get_point(750, 450)
    roof_list = [fist_point_window,second_point_window,therd_point_window]
    sd.polygon(point_list=roof_list, color=sd.COLOR_RED, width=0)
    fist_point_window = sd.get_point(450, 340)
    second_point_window = sd.get_point(1050, 340)
    therd_point_window = sd.get_point(750, 450)
    roof_list = [fist_point_window,second_point_window,therd_point_window]
    sd.polygon(point_list=roof_list, color=sd.COLOR_DARK_RED, width=3)
