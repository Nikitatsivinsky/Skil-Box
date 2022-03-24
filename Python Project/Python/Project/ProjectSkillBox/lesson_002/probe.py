my_pets = ['elifant', 'dog', 'murzik', 'cat', 'her']
i = 0
while i < len(my_pets):
    pet = my_pets[i]
    print('Check - ', pet)
    if pet == 'cat':
        print('Cat found!')
        break
    i += 1
    print(pet, ' is not a cat!')
print('Goodbuy!')