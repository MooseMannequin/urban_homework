class Animal:

    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if isinstance (self, Animal):

            if isinstance(food, Fruit):
                print(f'{self.name} съел {food.name}')
                self.fed = True
            else:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False


class Plant:

    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):
    pass

class Predator(Animal):
    pass
class Flower(Plant):
    pass
class Fruit(Plant):
    edible = True


Wolf = Predator('Волк')
Sheep = Mammal("Овца")
romashka = Flower('Ромашка')
Apple = Fruit('яблоко')

print(Sheep.name)
print(Sheep.alive)
Sheep.eat(Apple)
print(Sheep.fed)
print()

print(Wolf.name)
print(Wolf.alive)
Wolf.eat(romashka)
print(Wolf.fed)
