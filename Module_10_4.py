from queue import Queue
from threading import Thread
from time import sleep
from random import randint


class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    q = Queue()

    def __init__(self, *tables):
        self.tables = tables

    def guest_arrival(self, *guests):
        vacant_tables = []
        for table in self.tables:
            if table.guest is None:
                vacant_tables.append(table)
        for guest in guests:
            if len(vacant_tables) != 0:
                vacant_tables[0].guest = guest
                print(f'{guest.name} сел(-а) за стол номер {vacant_tables[0].number}')
                vacant_tables.remove(vacant_tables[0])
            else:
                self.q.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        vacant_tables = []
        while len(vacant_tables) != 0 or not self.q.empty():
            for table in self.tables:
                if table.guest is None:
                    vacant_tables.append(table)
                if table.guest is not None and not table.guest.is_alive():
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Стол номер {table.number} свободен')
                    table.guest = None
                    vacant_tables.append(table)
                    if not self.q.empty():
                        table.guest = self.q.get()
                        vacant_tables.remove(table)
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()




# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

