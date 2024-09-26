class Vehicle:

    __COLOR_VARIANTS = ['white', 'black', 'green', 'blue', 'YELLOW']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = str(owner)
        self.model = str(__model)
        self.color = str(__color)
        self.power = int(__engine_power)

    def new_owner(self, owner):
        self.owner = owner

    def get_model(self):
        print(f'Модель: {self.model}')

    def get_horsepower(self):
        print(f'Мощность двигателя: {self.power}')

    def get_color(self):
        print(f'Цвет: {self.color}')

    def print_info(self):
        self.get_model(), self.get_horsepower(), self.get_color()
        return f'Владелец: {self.owner}'

    def set_color(self, new_color):
        for i in self.__COLOR_VARIANTS:

            if str(new_color.lower()) == i.lower():
                self.color = new_color.lower()
                break

        if self.color != new_color.lower():
            print(f'Нельзя сменить цвет на {new_color.lower()}')


class Sedan(Vehicle):
    pass

Ford = Sedan('Andrew', 'Ford Focus', 'Red', 100)

print(Ford.print_info())
print()
Ford.set_color('yeLlOw')
Ford.new_owner('Lana')
print(Ford.print_info())

