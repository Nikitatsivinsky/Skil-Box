class Human():
    def __init__(self, name):
        self.name = name




tenants_list = ['Борис',
            'Манька',
            'Клара',
            'Батхед'
           ]

           # Kitty(name='Клара'),
           # Kitty(name='Батхед'),
           # Kitty(name='Кенни'),
           # Kitty(name='Кенни'),
          # ]
teants = []
counter_persons = 0
for person in tenants_list:
    if counter_persons < 2:
        x = Human(name=person)
        teants.append(x)
        counter_persons += 1

print(tenants_list)
print(teants)



