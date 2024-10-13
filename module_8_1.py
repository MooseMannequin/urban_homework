def add_everything_up(a,b):
    try:
        result = a + b
        return result.__round__(3)
    except:
        return str(a) + str(b)

print(add_everything_up(3, 5))
print(add_everything_up(3, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
