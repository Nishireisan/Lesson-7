#Словарь
my_dict = {'Frad': 2020, 'brad': 2004, 'Dabra': 1994, 'Goward': 1987}
print(my_dict)
print(my_dict.get('Frad'))
print(my_dict.get('Charli'))
my_dict.update({'Dan': 2003,
                'Fredi': 2000,
                'Joneon': 1950})
d = my_dict.pop('brad')
print(my_dict)
print(d)
#множества
my_set = {1, 2, 3.25, 4, 3, 2, 1, 'string', 1 > 5}
print(my_set)
my_set.add(9)
my_set.add(23)
my_set.discard(4)
print(my_set)
