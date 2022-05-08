#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
import math
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

moscow_london = round (math.sqrt((sites['Moscow'][0] - sites['London'][0]) ** 2 + (sites['Moscow'][1] - sites['London'][1]) ** 2))
london_paris = round (math.sqrt((sites['Paris'][0] - sites['London'][0]) ** 2 + (sites['Paris'][1] - sites['London'][1]) ** 2))
paris_moscow = round(math.sqrt((sites['Paris'][0] - sites['Moscow'][0]) ** 2 + (sites['Paris'][1] - sites['Moscow'][1]) ** 2))

distances_moscow = {'moscow_london_result' : moscow_london , 'paris_moscow_result' : paris_moscow}
distances_paris = { 'london_paris_result' : london_paris , 'paris_moscow_result' : paris_moscow}
distances_london = {'moscow_london_result' : moscow_london , 'london_paris_result' : london_paris }
distances = {'Moscow' : distances_moscow , 'Paris' : distances_paris , 'London' : distances_london }

pprint(distances)

