import threading
from time import sleep

class knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name, self.power = name, power

    def run(self):
        enemies = 100
        day = 0
        print(f'{self.name}, на нас напали!')
        while enemies > 0:
            day += 1
            sleep(1)
            enemies = enemies - self.power
            print(f'{self.name} сражается {day} дней, осталось {enemies} врагов\n')
        print(f'{self.name} Одержал победу спустя {day} дней')


knight1 = knight('Sir Lancelot', 10)
knight2 = knight("Sir Galahad", 20)

knight1.start()
knight2.start()

