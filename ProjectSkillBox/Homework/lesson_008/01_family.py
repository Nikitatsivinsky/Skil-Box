# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:
    money = 100
    food = 50
    dust = 0

    def __str__(self):
        return 'В доме: денег - {}, еды - {}, грязи - {}.'.format(self.money, self.food, self.dust)


class Human:
    fullness = 30
    smile = 100

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Я {} , сытость {}, счастье {}'.format(self.name, self.fullness, self.smile)


class Husband(Human, House):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if self.fullness < 30:
            self.eat()
        elif House.money < 100:
            self.work()
        else:
            self.gaming()

    def eat(self):
        if House.food > 0:
            eat_act = randint(15, 30)
            if House.food < eat_act:
                House.food = 0
                self.fullness += House.food
                print('{} доел остатки еды в доме!'.format(self.name))
            House.food -= eat_act
            self.fullness += eat_act
            print('{} покушал {} еды!'.format(self.name, eat_act))
        else:
            print('{} умер от нехватки еды!'.format(self.name))
            exit()



    def work(self):
        self.fullness -= 10
        House.money += 150
        print('{} сходил на работу!'.format(self.name))

    def gaming(self):
        self.fullness -= 10
        if self.smile < 1:
            print('{} умер от депрессии!'.format(self.name))
            exit()
        elif self.smile > 0:
            self.smile += 20
            print('{} играл целый день в танки!'.format(self.name))
        if self.smile > 100:
            self.smile = 100
            return


class Wife(Human, House):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        if House.dust > 90:
            self.smile -= 10

        if self.fullness < 30:
            self.eat()
        elif House.food < 70:
            self.shopping()
        elif House.dust > 60:
            self.clean_house()
        else:
            self.buy_fur_coat()

    def eat(self):
        if House.food > 0:
            eat_act = randint(15, 30)
            if House.food < eat_act:
                House.food = 0
                self.fullness += House.food
                print('{} доела остатки еды в доме!'.format(self.name))
            House.food -= eat_act
            self.fullness += eat_act
            print('{} покушала {} еды!'.format(self.name, eat_act))
        else:
            print('{} умерла от нехватки еды!'.format(self.name))
            exit()


    def shopping(self):
        self.fullness -= 10
        food_parametr = randint(90, 150)
        if House.money >= food_parametr:
            House.food += food_parametr
            House.money -= food_parametr
            print('{} сходила за покупками!'.format(self.name))
        elif House.money > 0:
            House.food += House.money
            House.money = 0
            print('{} купила продукты на последние деньги!'.format(self.name))

        else:
            print('{} пошла за покупками, но не хватило денег!'.format(self.name))

    def buy_fur_coat(self):
        self.fullness -= 10
        if self.smile < 1:
            print('{} умерла от депрессии!'.format(self.name))
            exit()
        if House.money > 410:
            self.smile += 60
            House.money -= 350
            print('{} купила себе шубу!'.format(self.name))
        else:
            print('{} пошла покупать себе шубу, но она слишком дорогая!'.format(self.name))

    def clean_house(self):
        self.fullness -= 10
        dust_parametr = randint(80, 100)
        House.dust -= dust_parametr
        if House.dust < 0:
            House.dust = 0
        print('{} поубирала в квартире!'.format(self.name))


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(366):
    House.dust += 5
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='blue')

# TODO после реализации первой части - отдать на проверку учителю
























######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass



























######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')

