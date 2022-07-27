# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#                 https://drive.google.com/file/d/1AlsYHIPCbMjDFmYNdAjLQEDOfjSI6tb-/view
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>


import os
from collections import defaultdict

from get_file_from_google_disk import GoogleDriveDownloader



class DictSortable(defaultdict):

    def sort_by_value(self, descending=False):

        sorted_values = sorted(self.values(), reverse=descending)
        sorted_dict = {}

        for i in sorted_values:
            for k in self.keys():
                if self[k] == i:
                    sorted_dict[k] = self[k]
                    break
        return sorted_dict

def analyze_ticker(f_name):
    with open(file=f_name, mode='r', encoding='utf-8') as file:
        price_max = None
        price_min = None
        skip_header = True
        first_values = True
        for line in file:
            secid, tradetime, price, quantity = line.split(",")
            if skip_header:
                skip_header = False
                continue

            if first_values:
                price_max = float(price)
                price_min = float(price)
                first_values = False
                continue

            if float(price) > price_max:
                price_max = float(price)

            if float(price) < price_min:
                price_min = float(price)

        average_price = (price_min + price_max) / 2
        volatility = round(((price_max - price_min) / average_price) * 100, 2)
    return volatility, secid


downloadeble_file_path = os.path.dirname(__file__) + "/" + 'trades.zip'
downloadeble_file_link = "https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing"
if not os.path.exists(downloadeble_file_path):
    GoogleDriveDownloader.download_file_from_google_drive(file_id=downloadeble_file_link,
                                                          dest_path=downloadeble_file_path, unzip=True)
trades_dir = os.path.dirname(__file__)+'/trades/'

ticker_list = []


for name in os.listdir(trades_dir):
    if os.path.isfile(trades_dir+name):
        ticker_list.append(trades_dir+name)

volatility_max_dict = {}
volatility_min_dict = {}

volatility_zero_dict = {}

tickers_general = DictSortable(float)


for ticker_path in ticker_list:
    volatility, secid = analyze_ticker(ticker_path)
    if volatility == 0:
        volatility_zero_dict[secid] = volatility
    else:
        tickers_general[secid] = volatility

i = 0
for key, value in tickers_general.sort_by_value(descending=True).items():
    if i < 3:
        volatility_max_dict[key] = value
    elif i >= len(tickers_general.sort_by_value(descending=True).items())-3:
        volatility_min_dict[key] = value
    i += 1


zero_dict_for_print = ', '.join(volatility_zero_dict)
print(" " * 3, 'Максимальная волатильность:')
for name, value in volatility_max_dict.items():
    print(f'{" " * 6}{name} - {value} %')
print(" " * 3, 'Минимальная волатильность:')
for name, value in volatility_min_dict.items():
    print(f'{" " * 6}{name} - {value} %')
print(" " * 3, 'Нулевая волатильность:')
print(f'{" " * 6}{zero_dict_for_print}')
