my_dict = {'Masha':1980, 'Misha':1977, 'Kolya':1987}
print('Dict: ',my_dict)
print(my_dict['Misha'])
print(my_dict .get('Rinat'))
my_dict.update({'Rinat':1981,
                'Garry':1988})
a = my_dict.pop('Kolya')
print(a)
print(my_dict)
my_set = {1,1,2,2,'город',4.3,'улица',6.67,7,7,(1,2,30)}
print('Set:', my_set)
my_set.add(11)
my_set.add('дом')
my_set.discard('город')
print(my_set)