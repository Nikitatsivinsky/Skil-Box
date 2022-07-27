# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
import os
from collections import defaultdict
from threading import Thread
import queue
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


class TickerAnalizer(Thread):

    def __init__(self, f_name, queue, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.f_name = f_name
        self.volatility, self.secid = None, None
        self.queue = queue

    def run(self):
        with open(file=self.f_name, mode='r', encoding='utf-8') as file:
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
        self.queue.put([volatility, secid])


class Main(Thread):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self.volatility_max_dict = {}
        self.volatility_min_dict = {}
        self.volatility_zero_dict = {}
        self.tickers_general = DictSortable(float)
        self.threads = []
        self.queue = queue.Queue()

    def run(self):
        for ticker_path in ticker_list:
            self.threads.append(TickerAnalizer(ticker_path, queue=self.queue))

        for thread in self.threads:
            thread.start()

        while True:
            try:
                volatility, secid = self.queue.get(timeout=1)
                if volatility == 0:
                    self.volatility_zero_dict[secid] = volatility
                else:
                    self.tickers_general[secid] = volatility
            except queue.Empty:
                if not any(thread.is_alive() for thread in self.threads):
                    break
        i = 0
        for key, value in self.tickers_general.sort_by_value(descending=True).items():
            if i < 3:
                self.volatility_max_dict[key] = value
            elif i >= len(self.tickers_general.sort_by_value(descending=True).items()) - 3:
                self.volatility_min_dict[key] = value
            i += 1

        for thread in self.threads:
            thread.join()

        self.print_result()

    def print_result(self):
        zero_dict_for_print = ', '.join(self.volatility_zero_dict)
        print(" " * 3, 'Максимальная волатильность:')
        for name, value in self.volatility_max_dict.items():
            print(f'{" " * 6}{name} - {value} %')
        print(" " * 3, 'Минимальная волатильность:')
        for name, value in self.volatility_min_dict.items():
            print(f'{" " * 6}{name} - {value} %')
        print(" " * 3, 'Нулевая волатильность:')
        print(f'{" " * 6}{zero_dict_for_print}')


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

result = Main()
result.start()
result.join()



# volatility_max_dict = {}
# volatility_min_dict = {}
# volatility_zero_dict = {}
#
# tickers_general = DictSortable(float)


# threads = []
# queue = queue.Queue()

# for ticker_path in ticker_list:
#     threads.append(TickerAnalizer(ticker_path, queue=queue ))
#
# for thread in threads:
#     thread.start()
#
# while True:
#         try:
#             volatility, secid = queue.get(timeout=1)
#             if volatility == 0:
#                 volatility_zero_dict[secid] = volatility
#             else:
#                 tickers_general[secid] = volatility
#         except queue.empty:
#             if not any(thread.is_alive() for thread in threads):
#                 break
#
# for thread in threads:
#     thread.join()

# i = 0
# for key, value in tickers_general.sort_by_value(descending=True).items():
#     if i < 3:
#         volatility_max_dict[key] = value
#     elif i >= len(tickers_general.sort_by_value(descending=True).items())-3:
#         volatility_min_dict[key] = value
#     i += 1
#
#
# print(volatility_max_dict)
# print(volatility_min_dict)
# print(volatility_zero_dict)