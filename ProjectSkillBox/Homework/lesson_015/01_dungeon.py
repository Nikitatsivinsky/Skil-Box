# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход

import json
import re
import sys
from datetime import datetime
from decimal import *
import csv


class GameEngine:

    def __init__(self, data):
        self.current_experience = 0
        self.remaining_time = '1234567890.0987654321'
        self.field_names = ['current_location', 'current_experience', 'current_date']
        self.time_playing = datetime.now()
        self.current_data = data
        self.current_location, self.dict_avalible_transit, self.list_mob = self.next_transit(self.current_data)
        self.csv_counter = 1

    def start(self):
        while True:
            self.journal_csv(self.current_location, self.current_experience, self.remaining_time)
            action = self.next_action()

            if action == 1:

                if self.list_mob != []:
                    counter = 1
                    for mob in self.list_mob:
                        print(f'Если хотите атаковать {mob} нажмите {counter}')
                        counter += 1
                    attack = int(input('Введите номер монстра: '))
                    self.attack_monster(self.list_mob[attack - 1])
                    mob = self.list_mob[attack - 1]

                    if type(self.current_data[self.current_location]) == list:
                        for i in self.current_data[self.current_location]:
                            if type(i) == dict:
                                continue
                            elif type(i) == list:
                                if mob in i:
                                    i.remove(mob)
                            else:
                                self.current_data[self.current_location].remove(mob)
                                break

                    self.current_location, self.dict_avalible_transit, self.list_mob = self.next_transit(
                        self.current_data)
                else:
                    print('В локации нет монстров')
                    self.current_location, self.dict_avalible_transit, self.list_mob = self.next_transit(
                        self.current_data)

            elif action == 2:
                location_list = []
                counter = 1
                for location in self.dict_avalible_transit:
                    print(f"Если хотите перейти в локацию {location} - введите {counter}")
                    counter += 1
                    location_list.append(location)
                location_flag = int(input('Введите номер локации: '))
                if location_flag > len(location_list):
                    print('Нет такой локации')
                    self.current_location, self.dict_avalible_transit, self.list_mob = self.next_transit(
                        self.current_data)
                else:
                    next_location_name = location_list[location_flag - 1]
                    self.player_performance(next_location_name)
                    self.current_data = self.dict_avalible_transit[next_location_name]
                    self.current_list_mob = self.list_mob
                    self.current_location, self.dict_avalible_transit, self.list_mob = self.next_transit(
                        self.current_data)

            elif action == 3:
                exit('Вы вышли из игры')

    def next_action(self):
        result = int(input('Выберите действие:\n1.Атаковать монстра\n2.Перейти в другую локацию\n3.Выход\n'))
        if result > 4 or result < 1:
            print('Некорректный ввод')
            self.next_action()
        else:
            return result

    def attack_monster(self, monster):
        print(f'Вы атаковали {monster}')
        self.player_performance(monster)

    def next_transit(self, value):

        dict_avalible_transit = {}
        list_mob = []

        for main_location, value in value.items():
            print('_____________________________________________________________')
            print(f'Вы находитесь в {main_location}')
            print(f'У вас {self.current_experience} опыта и осталось {self.remaining_time} секунд')
            print(f'Прошло уже {datetime.now() - self.time_playing}')

            if value == []:
                sys.exit("Локация пустая, игра окончена!")
            elif self.current_experience >= 280:
                print('_____________________________________________________________')
                print(
                    f'Вы победили!\nВаш результат {self.current_experience} опыта и осталось '
                    f'{self.remaining_time} секунд!')
                sys.exit()
            elif Decimal(self.remaining_time) <= Decimal('0'):
                print('_____________________________________________________________')
                print(
                    f'У вас закончилось время!\nВаш результат {self.current_experience} опыта и прошло '
                    f'{datetime.now() - self.time_playing} секунд!')
                sys.exit()

            print('Внутри вы видите:')

            for item in value:
                if type(item) == dict:
                    for location, value in item.items():
                        print(f'-- Вход в локацию: {location}')
                        dict_avalible_transit[location] = item
                elif type(item) == list:
                    for monster in item:
                        print(f'-- Монстра {monster}')
                        list_mob.append(monster)
                else:
                    print(f'-- Монстра {item}')
                    list_mob.append(item)
            return [main_location, dict_avalible_transit, list_mob]

    def player_performance(self, name_value):

        tm = re.search("tm+\d+", name_value)
        exp = re.search("exp+\d+", name_value)
        if tm is not None:
            tm = tm[0].strip('tm')
            self.remaining_time = (Decimal(self.remaining_time) - Decimal(tm))
        if exp is not None:
            exp = exp[0].strip('exp')
            self.current_experience = Decimal(self.current_experience) + Decimal(exp)

    def journal_csv(self, location, experience, time):
        with open('dungeon.csv', 'a', newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            if self.csv_counter == 1:
                writer.writerow(self.field_names)
                self.csv_counter += 1
            writer.writerow([location, experience, time])


if __name__ == '__main__':
    with open('dungeon.csv', 'w', newline='') as csv_file:
        pass
    with open('rpg.json', 'r') as f:
        data = json.load(f)
    game = GameEngine(data)
    game.start()
