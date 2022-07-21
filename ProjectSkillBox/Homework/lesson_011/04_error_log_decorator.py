# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'


def log_errors(file_name):
    def decoration_func(func):
        def catching_exceptions(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as exc:
                line_exc = f'<{func.__name__}> <{args}> <{type(exc).__name__}> <{exc}>'
                print(f'Записываю в {file_name} строку: {line_exc}')
                with open(file_name, mode='a') as log_file:
                    log_file.write(line_exc + '\n')
                func(*args, **kwargs)

        return catching_exceptions

    return decoration_func


# Проверить работу на следующих функциях

@log_errors(file_name='function_errors.log')
def perky(param):
    return param / 0


@log_errors(file_name='function_errors.log')
def check_line(line_to_check):
    name, email, age = line_to_check.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]

for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
try:
    perky(param=42)
except Exception as exc:
    print(f'Invalid format: {exc}')

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
