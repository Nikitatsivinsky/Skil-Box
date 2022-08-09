# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
#
# import os
# from PIL import Image, ImageDraw, ImageFont, ImageColor
# def make_ticket(fio, from_, to, date):
#
#     im = Image.open(file_write)
#     draw = ImageDraw.Draw(im)
#     font = ImageFont.truetype(font_path, size=20)
#     write_list = [fio, from_, to]
#
#     y = im.size[1] - 218 - (10 + font.size) * 2
#     x = 45
#
#     for word in write_list:
#         paint_ticket(word,draw,font,y,x)
#         y += font.size + 48
#
#     y += font.size - 88
#     x = 260
#     paint_ticket(date, draw, font, y, x)
#     im.show()
#     im.save('ticket_template_test.png')
#     print(f'Post card saved az {os.path.dirname(__file__)}')
#
# def paint_ticket(message,draw,font,y,x):
#
#     draw.text((x, y), message, font=font, fill=ImageColor.colormap['black'])
#
#
# file_write = os.path.join("images", "ticket_template.png")
# font_path = os.path.join("images", "Spectral.ttf")
# make_ticket('Иванов Иван Иванович', 'Москва', 'Париж', '10.10.2020')

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля agrparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor

def make_ticket(fio, from_, to, date):
    im = Image.open(file_write)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, size=20)
    write_list = [fio, from_, to]

    y = im.size[1] - 218 - (10 + font.size) * 2
    x = 65

    for word in write_list:
        paint_ticket(word, draw, font, y, x)
        y += font.size + 48

    y += font.size - 88
    x = 260
    paint_ticket(date, draw, font, y, x)
    im.show()
    try:
        im.save(args.save_to)
    except FileNotFoundError:
        os.mkdir('/'.join(args.save_to.split('/')[:-1]))
        im.save(args.save_to)
    print(f'Сохранено в папке: {args.save_to}')


def paint_ticket(message, draw, font, y, x):
    draw.text((x, y), message, font=font, fill=ImageColor.colormap['black'])

parser = argparse.ArgumentParser(description='Print ticket script')
parser.add_argument('--fio', type=str, required=True, help='Name, Surname, Patronymic of the passenger', nargs=2)
parser.add_argument('--from_',type=str,  required=True, help='From which country')
parser.add_argument('--to',type=str,  required=True, help='To which country')
parser.add_argument('--date',type=str,  required=True, help='Date of departure')
parser.add_argument('--save_to', default=os.path.join(os.path.dirname(__file__), 'images', 'ticket_template_test.png'),
                    help='Path to save the filled ticket')

args = parser.parse_args()
file_write = os.path.join("images", "ticket_template.png")
font_path = os.path.join("images", "Spectral.ttf")
make_ticket = make_ticket(' '.join(args.fio), args.from_, args.to, args.date)
