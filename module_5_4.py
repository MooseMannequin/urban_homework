class house:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)


    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            print("нужно целочисленное значение")
        else:
            return self.number_of_floors + value

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

    def go_to(self, new_floor):
        floor_at = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor_at in range(new_floor):
                floor_at += 1
                print(floor_at)



elbrus = house("ЖК Эльбрус", 30)
print(house.houses_history)
mohave = house("ЖК Мохаве", 15)
print(house.houses_history)
del mohave
del elbrus
crimson = house("ЖК Кримзон", 5)
print(house.houses_history)

# elbrus.go_to(18)
# mohave.go_to(18)
# print(len(elbrus))
# print(str(mohave))
# print()
#
# mohave.number_of_floors = mohave + 12
# print(mohave)
# elbrus.number_of_floors = 3 + elbrus
# print(elbrus)
# elbrus.number_of_floors += 2
# print(elbrus)
# print(elbrus == mohave)
# print(elbrus != mohave)
# print(elbrus >= mohave)
# print(elbrus <= mohave)
# print(elbrus > mohave)
# print(elbrus < mohave)


