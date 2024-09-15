from threading import Thread
from time import sleep


class Knight(Thread):
    num_of_enemies = 100

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power


    def run(self):
        print(f'{self.name}, на нас напали!')
        days_counter = 0
        while self.num_of_enemies > 0:
            self.num_of_enemies -= self.power
            days_counter += 1
            sleep(1)
            if self.num_of_enemies >= 0:
                print(f'{self.name} сражается {days_counter} день(дня)..., '
                      f'осталось {self.num_of_enemies} воинов.\n')
            else:
                print(f'{self.name} сражается {days_counter} день(дня)..., '
                      f'осталось 0 воинов.\n')


        print(f'{self.name} одержал победу спустя {days_counter} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print(f'Все битвы закончились!')


