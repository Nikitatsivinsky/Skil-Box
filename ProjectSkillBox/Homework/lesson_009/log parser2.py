from datetime import datetime


class LogFile:
    __name = None
    log_entries = []
    log_entries_grp = {}

    def __init__(self, file_name):
        self.set_name(file_name)

    def set_name(self, file_name):
        self.__name = file_name

    def get_name(self):
        return self.__name

    def write_to_file(self, file):
        for lg in self.log_entries_grp.items():
            time_value = lg[0].strftime("%Y-%m-%d %H:%M")
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

    def group(self):
        for e in self.log_entries:
            if e.is_not_ok():
                date_round = e.date
                date_round = date_round.replace(microsecond=0, second=0) # datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]
                if not (date_round in self.log_entries_grp):
                    self.log_entries_grp[date_round] = 1
                else:
                    self.log_entries_grp[date_round] += 1







x = LogNOKGroupByMinute('events.txt')

with open("result.txt", mode='w+', encoding='utf8') as file:
    file.write(f"{'*' * 10} Start Analyzing file {'events.txt'}!{'*' * 10}\n\n")
    x.write_to_file(file)
