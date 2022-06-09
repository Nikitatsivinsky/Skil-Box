# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class OpenFile():
    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        result_analized = Analized(OpenFile)
        with open(file=self.file_name, mode='r', encoding="utf8") as file:
            for line in file:
                result_analized.analized(line=line, file_name=self.file_name)


class Analized(OpenFile):
    log_event_counter = 0
    log_list = {'time_event': 0, 'counter': 0}
    prev_log_time = None

    def analized(self, line, file_name):
        if "NOK" in line:
            log_time = line[1:17]

            if log_time == self.prev_log_time:
                self.log_list['time_event'] = log_time
                self.log_list['counter'] += 1
            else:
                self.Result_to_TXT(self.log_list, file_name)
                self.log_list['time_event'] = log_time
                self.log_list['counter'] = 1

            self.prev_log_time = log_time

    def Result_to_TXT(self, log_list, file_name):
        result_txt_file_name = 'result.txt'
        with open(result_txt_file_name, mode='a', encoding='utf8') as file:
            if log_list['time_event'] == 0:
                file.write(f"{'*' * 10} Start Analyzing file {file_name}!{'*' * 10}\n\n")
            else:
                file.write('[' + str(log_list['time_event']) + ']' + '  ' + str(log_list['counter']) + '\n')

        return


open_file = OpenFile(file_name="events.txt")
open_file.open_file()


# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
