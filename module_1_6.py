my_dict = {'Lena': 1998, 'Misha': 1964, 'Vlad': 2003}
print(my_dict)
print(my_dict.get('Lena'), my_dict.get('Vera'))
my_dict.update({'Vera': 2005, 'Gleb': 1983})
Popped = my_dict.pop('Misha')
print(Popped)
print(my_dict)

my_set = {2,2,3,3,True,True,'String','String'}
print(my_set)
my_set.add((0,1,2,3))
my_set.add('Set')
print(my_set)
my_set.discard('Set')
print(my_set)