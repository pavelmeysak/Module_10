from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            all_data.append(file.readline().strip('\n'))
            if not file.readline().strip('\n'):
                break


filenames = [f'./file {number}.txt' for number in range(1, 5)]

#  Линейный способ

start_1 = datetime.now()
for name in filenames:
    read_info(name)
end_1 = datetime.now()
print(end_1-start_1)

#  С помощью процессов
if __name__ == '__main__':
    with Pool(processes=4) as pool:
        start_2 = datetime.now()
        pool.map(read_info, filenames)
    end_2 = datetime.now()
    print(end_2-start_2)












