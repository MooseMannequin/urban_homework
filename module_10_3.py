import threading
from random import randint
from time import sleep


class bank:
    def __init__(self):
        pass

    balance = 0
    lock = threading.Lock()
    def deposit(self):
        for _ in range(100):
            sum_d = randint(50, 500)
            self.balance += sum_d
            print(f'Пополнение {sum_d}. Баланс {self.balance}')
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            sleep(0.001)



    def take(self):
        for _ in range(100):
            sum_t = randint(50, 500)
            print(f'Запрос на {sum_t}\n')
            if sum_t <= self.balance and self.balance >= 500:
                self.balance -= sum_t
                print(f'Снятие {sum_t}. Баланс {self.balance}.')
            else:
                if self.lock.locked() == True:
                    print(f'Запрос отклонён, недостаточно средств')
                else:
                    print(f'Запрос отклонён, недостаточно средств')
                    self.lock.acquire()
            sleep(0.001)


bank1 = bank

thread1 = threading.Thread(target=bank.deposit, args=(bank1,))
thread2 = threading.Thread(target=bank.take, args=(bank1,))

thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(f'Итоговый баланс: {bank1.balance}')