import argparse


class BowlingScoreEngine:

    def __init__(self, game_result: str):

        if game_result == None:
            raise TypeError('Вызовите скрипт с параметром!')

        self.game_result = game_result
        self.score = 0
        self.get_score()
        self.frame = 0

    def __str__(self):
        return f'Счет: {self.score}'

    def get_score(self):
        one_frame_counter = 0
        try:
            for val in self.game_result:

                if val == 'Х' or val == 'Х':
                    self.score += 20
                    self.frame += 1
                elif val == '/':
                    self.score -= int(self.game_result[self.game_result.index(val) - 1])
                    self.score += 15
                    self.frame += 1
                elif val == '-':
                    self.score += 0
                    one_frame_counter += 1
                elif int(val) in range(1, 10):
                    self.score += int(val)
                    one_frame_counter += 1
                else:
                    self.raise_error(val)

                if one_frame_counter == 2:
                    self.frame += 1
                    one_frame_counter = 0

                if self.frame > 10:
                    raise ValueError('Количество фреймов превышает 10!')
        except Exception as exc:
            self.raise_error(val, exc)

    def raise_error(self, val, exc=None):

        list_of_invalid_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '<',
                                   '>', '?', '.', ',', ';', "'", '[', ']', '\\', '=', '`', '~']


        if "'" in val or '"' in val:
            raise ValueError(f'Неверный формат данных, при вызове функции с параметром '
                             f'не используйте кавычки: <{val}>!')
        elif val in list_of_invalid_symbols:
            raise ValueError(f'Неверный формат данных, в запросе присутствует неверный символ- "{val}"! \n'
                             f'Возможно вы вызвали функцию с пустым параметром!')
        elif val.isalpha():
            raise ValueError(f'Неверный формат данных, в запросе присутствует неверная буква - "{val}"!')
        elif val == "0":
            raise ValueError(f'Неверный формат данных, в запросе присутствует неверное число - "{val}"!')
        else:
            raise ValueError(f'Неверный формат данных: {exc}')

if __name__ == '__main__':
    """
    argparser
    """
    parser = argparse.ArgumentParser(description='Подсчет очков в игре Боулинг')
    parser.add_argument('--result', type=str, help='Результат игры')
    args = parser.parse_args()
    print(BowlingScoreEngine(args.result))





