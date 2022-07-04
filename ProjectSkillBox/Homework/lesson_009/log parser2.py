from datetime import datetime

class LogFile:
    __name = None
    log_entries = []
    log_entries_grp = {}
    time_format = "%Y-%m-%d %H:%M:%S.%f"


    def __init__(self, file_name):
        self.set_name(file_name)

    def set_name(self, file_name):
        self.__name = file_name

    def get_name(self):
        return self.__name

    def write_to_file(self, file):
        for lg in self.log_entries_grp.items():
            time_value = lg[0].strftime(self.time_format)
            file.write(f'[{time_value}] {lg[1]}' + '\n')


class LogEntry:
    date = None
    value = None

    def __init__(self, line):
        time_text = str(line[1:27])
        self.date = datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S.%f")
        self.value = str(line[29:]).strip()

    def to_txt(self):
        return f'{self.date} {self.value}'


class LogEntryNOK(LogEntry):

    def is_not_ok(self):
        return self.value == 'NOK'


class LogNOK(LogFile):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.read_from_file()

    def read_from_file(self):
        with open(file=self.get_name(), mode='r', encoding="utf8") as file:
            for line in file:
                self.log_entries.append(LogEntryNOK(line))


class LogNOKGroupByMinute(LogNOK):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.group()
        self.time_format = "%Y-%m-%d %H:%M"

    def group(self):
        for e in self.log_entries:
            if e.is_not_ok():
                date_round = e.date
                date_round = date_round.replace(microsecond=0, second=0)
                if not (date_round in self.log_entries_grp):
                    self.log_entries_grp[date_round] = 1
                else:
                    self.log_entries_grp[date_round] += 1


class LogNOKGroupByHour(LogNOK):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.group()
        self.time_format = "%Y-%m-%d %H"

    def group(self):
        for e in self.log_entries:
            if e.is_not_ok():
                date_round = e.date
                date_round = date_round.replace(microsecond=0, second=0, minute=0)
                if not (date_round in self.log_entries_grp):
                    self.log_entries_grp[date_round] = 1
                else:
                    self.log_entries_grp[date_round] += 1

class LogNOKGroupByDay(LogNOK):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.group()
        self.time_format = "%Y-%m-%d"

    def group(self):
        for e in self.log_entries:
            if e.is_not_ok():
                date_round = e.date
                date_round = date_round.replace(microsecond=0, second=0, minute=0, hour=0)
                if not (date_round in self.log_entries_grp):
                    self.log_entries_grp[date_round] = 1
                else:
                    self.log_entries_grp[date_round] += 1

class LogNOKGroupByMonth(LogNOK):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.group()
        self.time_format = "%Y-%m"

    def group(self):
        for e in self.log_entries:
            if e.is_not_ok():
                date_round = e.date
                date_round = date_round.replace(microsecond=0, second=0, minute=0, hour=0, day=1)
                if not (date_round in self.log_entries_grp):
                    self.log_entries_grp[date_round] = 1
                else:
                    self.log_entries_grp[date_round] += 1

class LogNOKGroupByYear(LogNOK):

    def __init__(self, file_name):
        super().__init__(file_name)
        self.group()
        self.time_format = "%Y"

    def group(self):
        for e in self.log_entries:
            if e.is_not_ok():
                date_round = e.date
                date_round = date_round.replace(microsecond=0, second=0, minute=0, hour=0, day=1, month=1)
                if not (date_round in self.log_entries_grp):
                    self.log_entries_grp[date_round] = 1
                else:
                    self.log_entries_grp[date_round] += 1


flag_mode = input(f'Введите 1 если хотите отсортировать файл по минутам\n'
                  f'Введите 2 если хотите отсортировать файл по часам \n'
                  f'Введите 3 если хотите отсортировать файл по дням\n'
                  f'Введите 4 если хотите отсортировать файл по месяцам\n'
                  f'Введите 5 если хотите отсортировать файл по годам\n')

file_name_result = input(f'Введите 1 если хотите использовать стандартное название файла (result.txt)\n'
                  f'Введите 2 если хотите использовать свое название файла\n')

if int(file_name_result) == 1:
    file_name_result = 'events.txt'
elif int(file_name_result) == 2:
    file_name_result = input(f'Введите свое название файла. Без расширения файла!(.txt)\n')
    file_name_result.strip()
    if '.txt' in file_name_result:
        exit(f'Введено неверное название файла. Вводить нужно только имя. без расширения файла (.txt)')
    file_name_result = file_name_result + '.txt'
else:
    exit(f'Введено неверное название файла')


if int(flag_mode) == 1:
    method_sort = LogNOKGroupByMinute('events.txt')
elif int(flag_mode) == 2:
    method_sort = LogNOKGroupByHour('events.txt')
elif int(flag_mode) == 3:
    method_sort = LogNOKGroupByDay('events.txt')
elif int(flag_mode) == 4:
    method_sort = LogNOKGroupByMonth('events.txt')
elif int(flag_mode) == 5:
    method_sort = LogNOKGroupByYear('events.txt')
else:
    exit(f'Введено неверное значение выбора сортировки')

with open(file_name_result, mode='w+', encoding='utf8') as file:
    file.write(f"{'*' * 10} Start Analyzing file {'events.txt'}!{'*' * 10}\n\n")
    method_sort.write_to_file(file)
