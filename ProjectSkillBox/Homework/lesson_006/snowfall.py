import simple_draw as sd
import random

list_coordinates = []
length_snow = []
abc_list = []

fallen_list = []
snowflakes_fallen_lengths = []
abc_list_fallen = []

number = 0
point = None
point2 = None

def make_snowfall_list(N):
    global list_coordinates
    global length_snow
    global abc_list

    for counter in range(N):
        list_coordinates.append([sd.random_number(100, 1200), sd.random_number(800, 1300)])
        length_snow.append(sd.random_number(20, 70))
        abc_list.append(
            [round(random.uniform(0.3, 1), 1), round(random.uniform(0.15, 0.55), 2), sd.random_number(50, 70)])

def make_snowfall_background():
    global point
    point = sd.get_point(list_coordinates[number][0], list_coordinates[number][1])
    sd.start_drawing()

    print(list_coordinates)
    print(length_snow)
    print(abc_list)

    sd.snowflake(center=point, length=length_snow[number], color=sd.background_color, factor_a=abc_list[number][0],
                 factor_b=abc_list[number][1], factor_c=abc_list[number][2])


def move_snowfall_in_list():

    global point2

    if list_coordinates[number][1] >= length_snow[number]:
        list_coordinates[number][1] -= sd.randint(20, 40)
        left_or_right_rand = sd.randint(0, 2)
        if left_or_right_rand < 0.5:
            list_coordinates[number][0] -= sd.randint(7, 10)
        else:
            list_coordinates[number][0] += sd.randint(7, 10)

        point2 = sd.get_point(list_coordinates[number][0], list_coordinates[number][1])


def make_snowfall():

    sd.snowflake(center=point2, length=length_snow[number], color=sd.COLOR_WHITE, factor_a=abc_list[number][0],
                 factor_b=abc_list[number][1], factor_c=abc_list[number][2])

def list_fallen():

    fallen_list.append([list_coordinates[number][0], list_coordinates[number][1]])
    snowflakes_fallen_lengths.append(length_snow[number])
    abc_list_fallen.append(
        [abc_list[number][0], abc_list[number][1], abc_list[number][2]])
    snowflakes_fallen_lengths.append(length_snow[number])

    list_coordinates.pop(number)
    length_snow.pop(number)
    abc_list.pop(number)

    length_snow.append(sd.random_number(20, 70))
    list_coordinates.append([sd.randint(0, 1200), 800 + 50])
    abc_list_fallen.append([round(random.uniform(0.3, 1), 1), round(random.uniform(0.15, 0.55), 2),
                            sd.random_number(50, 70)])

    for i in range(len(fallen_list)):
        point = sd.get_point(fallen_list[i][0], fallen_list[i][1])
        sd.snowflake(center=point, length=snowflakes_fallen_lengths[i], color=sd.COLOR_WHITE,
                     factor_a=abc_list[i][0], factor_b=abc_list[i][1], factor_c=abc_list[i][2])



N = 3

make_snowfall_list(N)
print(list_coordinates)
print(length_snow)
print(abc_list)
while True:

    make_snowfall_background()
    move_snowfall_in_list()
    make_snowfall()
    list_fallen()


sd.pause()