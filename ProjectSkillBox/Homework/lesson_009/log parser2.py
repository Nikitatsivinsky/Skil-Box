from datetime import datetime
from datetime import timedelta


class LogFile:

    __name = None

    def __init__(self, file_name):
        self.set_name(file_name)

    def set_name(self, file_name):
        self.__name = file_name

    def get_name(self):
        return self.__name


class LogEntry:
    date = None
    value = None

    def __init__(self, line):
        time_text = str(line[1:27])
        self.date = datetime.strptime(time_text, "%Y-%m-%d %H:%M:%S.%f")
        self.date.resolution = timedelta(seconds=1)
        self.value = str(line[29:]).strip()                        

    def to_txt(self):
        return f'{self.date} {self.value}'


class LogEntryNOK(LogEntry):

    def is_not_ok(self):
        return self.value == 'NOK'


class LogNOK(LogFile):

    log_entries = []

    def __init__(self, file_name):
        super().__init__(file_name)
        self.read_from_file()

    def read_from_file(self):
        with open(file=self.get_name(), mode='r', encoding="utf8") as file:
            for line in file:
                self.log_entries.append(LogEntryNOK(line))

class LogNOKGroupByMinute(LogNOK):

    log_entries_grp = []

    def __init__(self, file_name):
        super().__init__(file_name)

    def group(self):
        for e in self.log_entries:
            if e.is_not_ok():
                e_round = e
                e_round.date.microsecond = 0  # datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]
                e_round.date.second = 0
                if not e_round in self.log_entries_grp:
                    self.log_entries_grp.append(e_round)









x = LogNOK('events.txt')





