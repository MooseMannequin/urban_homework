import threading
from random import randint
from time import sleep
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
            sleep(randint(3, 10))

class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests[0:len(self.tables)]:
            self.queue.put(guest)
            for Table in self.tables:
                if Table.guest == None:
                    Table.guest = self.queue.get()
                    print(f'{Table.guest.name} сел за стол {Table.number}')
                    Table.guest.start()
                    break
                else:
                    continue
        print()
        for guest in guests[len(self.tables):]:
            self.queue.put(guest)
            print(f'{guest.name} в очереди')
        print()

    def discuss_guests(self):
        serving = True
        while not self.queue.empty() or serving == True:
            for Table in self.tables:
                if Table.guest != None and Table.guest.is_alive() == False:
                    print(f'{Table.guest.name} покушал и ушел\n' f'Стол номер {Table.number} свободен\n')
                    Table.guest = None
                else:
                    continue
                if self.queue.empty() == False:
                    Table.guest = self.queue.get()
                    print(f'{Table.guest.name} вышел из очереди и сел за стол номер {Table.number}\n')
                    Table.guest.start()
            for Table in self.tables:
                if Table.guest != None:
                    serving = True
                    break
                else:
                    serving = False





tables = [Table(number) for number in range(1, 6)]

guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

guests = [Guest(name) for name in guests_names]

cafe = Cafe(*tables)

cafe.guest_arrival(*guests)

cafe.discuss_guests()
