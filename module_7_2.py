
def custom_write(file_name = 'test.txt', strings =
                ['Text for tell.',
                'Используйте кодировку utf-8.',
                'Because there are 2 languages!',
                'Спасибо!']):
    file = open(file_name, 'r+', encoding='utf-8')
    strings_positions = {}
    string_num = 1
    for string in strings:
        strings_positions[(string_num, file.tell())] = string
        string_num += 1
        file.write (f'{string}\n')

    file.close()

    return print(strings_positions)

custom_write()