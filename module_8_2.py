
def personal_sum(numbers):
    incorrect_data = 0
    result = 0
    for number in numbers:
        try:
            result = result + number
        except:
            incorrect_data = incorrect_data + 1
            print(f'Некорректный тип данных для подсчёта суммы - {number}')
    return result, incorrect_data


def calculate_average(numbers):
    divider = 0
    try:
        summ = personal_sum(numbers)
        for number in numbers:
            if isinstance(number, int) or isinstance(number, float):
                    divider += 1
        try:
            return (summ[0] / divider).__round__(2)
        except ZeroDivisionError:
            return 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных')
        return None


print(calculate_average((22, 33)))
print(calculate_average(33))
print(calculate_average((4, 6, 23.666, 'собака', 0, -1, 'пупупу')))
print(calculate_average(('собака','пупупу')))

