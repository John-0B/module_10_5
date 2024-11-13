import time
import multiprocessing as mult
from pprint import pprint


def read_info(name):
    all_data = []
    with open(name) as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)


filenames = [f'file {number}.txt' for number in range(1, 5)]
start = time.time()
read = [read_info(name) for name in filenames]
print('Линейный вызов', time.time() - start)

if __name__ == '__main__':
    start1 = time.time()
    with mult.Pool(4) as p:
        p.map(read_info, filenames)
    print('Многопроцессный', time.time() - start1)
