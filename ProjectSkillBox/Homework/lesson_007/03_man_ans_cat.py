# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.

class Human:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.energy = 100

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food_human >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food_human -= 10
            self.energy += 40
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 20
        self.energy -= 40

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.energy += 10

    def sleep(self):
        cprint('{} энергия равна {}'.format(self.name, self.energy), color='green')
        cprint('{} устал и лег спать'.format(self.name), color='green')
        self.energy += 100

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_human  += 50
            self.energy -= 20
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_zoo(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за кормом'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food_kitty += 50
            self.energy -= 20
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def clean(self):
        if self.house.dust > 30:
            cprint('{} поубирал в доме'.format(self.name), color='magenta')
            self.house.dust -= 70
            self.fullness -= 20
            self.energy -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        self.energy -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 20:
            self.eat()
        elif self.house.food_human < 20:
            self.shopping()
        elif self.house.food_kitty < 50:
            self.shopping_zoo()
        elif self.energy < 50:
            self.sleep()
        elif self.house.money < 50:
            self.work()
        elif self.house.dust > 30:
            self.clean()
        else:
            self.watch_MTV()

class Kitty:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.energy = 100

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food_kitty >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 20
            self.house.food_kitty -= 10
            self.energy += 5
        else:
            cprint('{} нет еды'.format(self.name), color='red')


    def sleep(self):
        cprint('{} энергия равна {}'.format(self.name,self.energy), color='green')
        cprint('{} спит целый день'.format(self.name), color='green')
        self.fullness -= 10
        self.energy += 100

    def play(self):
        cprint('{} опять дерет обои'.format(self.name), color='green')
        self.fullness -= 20
        self.energy -= 30
        self.house.dust += 20


    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        self.energy -= 10
        cprint('Подобрал, кота {}.'.format(self.name), color='cyan')
        cprint('Добро пожпловать в семью!.'.format(), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        if self.fullness < 20:
            self.eat()
        elif self.energy < 20:
            self.sleep()
        else:
            self.play()


class House:

    def __init__(self):
        self.food_human = 50
        self.food_kitty = 0
        self.dust = 0
        self.money = 0

    def __str__(self):
        return 'В доме еды осталось {},корма осталось {}, денег осталось {}, в доме грязно на {}'.format(
            self.food_human, self.food_kitty, self.money,self.dust)


citizens = [Man(name='Борис')]


my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(my_sweet_home)

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
