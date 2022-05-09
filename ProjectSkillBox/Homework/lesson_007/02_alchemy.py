# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())

class Water():

    def __init__(self):
        self.name = 'Вода'

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Ground):
            return Dirt()
        else:
            return None

class Air():

    def __init__(self):
        self.name = 'Воздух'

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        else:
            return None

class Fire():

    def __init__(self):
        self.name = 'Огонь'

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Ground):
            return Lava()
        else:
            return None

class Ground():

    def __init__(self):
        self.name = 'Земля'

    def __str__(self):
        return f"{self.name}"

    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None



class Storm():

    def __init__(self):
        self.name = 'Шторм'

    def __str__(self):
        return f"{self.name}"


class Steam():

    def __init__(self):
        self.name = 'Пар'

    def __str__(self):
        return f"{self.name}"


class Dirt():

    def __init__(self):
        self.name = 'Грязь'

    def __str__(self):
        return f"{self.name}"


class Lightning():

    def __init__(self):
        self.name = 'Молния'

    def __str__(self):
        return f"{self.name}"


class Dust():

    def __init__(self):
        self.name = 'Пыль'

    def __str__(self):
        return f"{self.name}"


class Lava():

    def __init__(self):
        self.name = 'Лава'

    def __str__(self):
        return f"{self.name}"



print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Ground(), '=', Water() + Ground())

print(Fire(), '+', Air(), '=', Fire() + Air())
print(Fire(), '+', Water(), '=', Fire() + Water())
print(Fire(), '+', Ground(), '=', Fire() + Ground())

print(Air(), '+', Water(), '=', Air() + Water())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Ground(), '=', Air() + Ground())

print(Ground(), '+', Water(), '=', Ground() + Water())
print(Ground(), '+', Air(), '=', Ground() + Air())
print(Ground(), '+', Fire(), '=', Ground() + Fire())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
