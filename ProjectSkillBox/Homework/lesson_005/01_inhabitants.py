# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...
import room_1,room_2

def residents(folks, house):
    for human in folks:
        print('В комнате ', house.__name__ , ' живет: ', human)


residents(folks=room_1.folks, house= room_1)
residents(folks=room_2.folks, house= room_2)

