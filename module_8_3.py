class car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.vin = __vin
        self.numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__vin)

    def __is_valid_vin(self, vin_number):
        vin_number = self.vin
        if not isinstance(vin_number, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if vin_number < 1000000 or vin_number > 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')

    def __is_valid_numbers(self, numbers):
        numbers = self.numbers
        if not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(numbers) < 6 or len(numbers) > 6:
            raise IncorrectCarNumbers('Неверная длина номера')


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message
class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


try:
    car1 = car('Ford', 134875, 300)
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{car1.model} успешно создан')

try:
    car2 = car('Volkswagen', 1775884, 'n30h40')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{car2.model} успешно создан')

try:
    car3 = car('Renault', 1039994, 'тр68л0922')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{car2.model} успешно создан')

