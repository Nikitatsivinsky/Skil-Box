import argparse


class BowlingScoreEngine:

    def __init__(self, game_result: str):
        if type(game_result) != str:
            raise TypeError('Неверный формат данных, укажите в str!')
        self.game_result = game_result
        self.score = 0
        self.get_score()

    def __str__(self):
        return f'Счет: {self.score}'

    def get_score(self):

        try:
            for val in self.game_result:
                if val == 'Х':
                    self.score += 20
                elif val == '/':
                    self.score -= int(self.game_result[self.game_result.index(val) - 1])
                    self.score += 15
                elif val == '-':
                    self.score += 0
                elif int(val) in range(1, 10):
                    self.score += int(val)
                else:
                    self.raise_error(val)
        except Exception as exc:
            self.raise_error(val, exc)

    def raise_error(self, val, exc=None):

        list_of_invalid_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '|', ':', '<',
                                   '>', '?', '.', ',', ';', "'", '[', ']', '\\', '=', '`', '~']

        if val in list_of_invalid_symbols:
            raise ValueError(f'Неверный формат данных, в запросе присутствует неверный символ- "{val}"!')
        elif val.isalpha():
            raise ValueError(f'Неверный формат данных, в запросе присутствует неверная буква - "{val}"!')
        elif val == "0":
            raise ValueError(f'Неверный формат данных, в запросе присутствует неверное число - "{val}"!')
        else:
            raise ValueError(f'Неверный формат данных: {exc}')

game_result = "0"

if __name__ == '__main__':
    print(BowlingScoreEngine(game_result))






















    # """
    #     argparser
    #                 """
    # parser = argparse.ArgumentParser(description='Подсчет очков в игре Боулинг')
    # parser.add_argument('game_result', type=str, help='Результат игры')
    # args = parser.parse_args()



