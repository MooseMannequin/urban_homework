class house:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for floor_at in range(new_floor):
                floor_at += 1
                print(floor_at)



elbrus = house("ЖК Эльбрус", 30)
mohave = house("ЖК Мохаве",15)
elbrus.go_to(18)
mohave.go_to(18)
