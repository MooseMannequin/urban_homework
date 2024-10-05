from pprint import pprint

class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category


    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

class Shop:
    __file_name = 'product.txt'

    def add(self, *products):
        # file = open(self.__file_name, 'r+')
        # list_ = file.read()
        # file.close()
        for product in products:
            file = open(self.__file_name, 'r+')
            list_ = file.read()
            if product.name not in list_:
                file.write(f'{product}\n')
                file.close()
            else:
                print(f'Продукт {product} уже есть в магазине')

        file.close()


    def get_products(self):
        file = open(self.__file_name, 'r')
        list_ = file.read()
        file.close()
        return list_




veg_shop = Shop()
potatoes = Product('Potatoes', 30.6, 'Vegetables')
carrots = Product('Carrots', 17.3, 'Vegetables')
potatoes_red = Product('Potatoes', 33.7, 'Vegetables')


print(veg_shop.get_products())
veg_shop.add(potatoes, carrots, potatoes_red)
print(veg_shop.get_products())


