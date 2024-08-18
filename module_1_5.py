immutable_var = ('string', 1, False)
print(immutable_var)
# immutable_var[0] = 'new string'
# print(immutable_var)
# Элементы Кортежа, которые не являются списком, нельзя изменить,
# потому что они неизменяемые
mutable_list = ['mut_string', 33, True]
print(mutable_list)
mutable_list[0] = 'new mut_string'
mutable_list[2] = False
print(mutable_list)