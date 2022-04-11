import simple_draw as sd
import random





def snow():
    num = 0
    while True:
        x = sd.random_number(10, 450)
        y = sd.random_number(0, 100)
        point = sd.get_point(x, y)
        length_snow = (sd.random_number(10, 20))
        fac_a = (random.uniform(0.3, 1))
        fac_b = (random.uniform(0.15, 0.55))
        fac_c = sd.random_number(50, 70)
        sd.snowflake(center=point, length=length_snow, color=sd.COLOR_WHITE,
                             factor_a=fac_a, factor_b=fac_b, factor_c=fac_c)
        num += 1
        if num > 200:
            break