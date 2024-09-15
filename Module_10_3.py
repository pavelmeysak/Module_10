from threading import Thread, Lock
from time import sleep
from random import randint


class Bank:
    lock = Lock()
    balance = 0

    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            add_val = randint(50, 500)
            self.balance += add_val
            print(f'Пополнение: {add_val}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            take_val = randint(50, 500)
            print(f'Запрос на {take_val}')
            if take_val <= self.balance:
                self.balance -= take_val
                print(f'Снятие: {take_val}. Баланс: {self.balance}')
                sleep(0.001)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')






