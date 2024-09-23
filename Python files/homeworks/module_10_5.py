import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

def linear_execution(filenames):
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    print(f"Линейное выполнение заняло: {time.time() - start_time:.5f} секунд")

def parallel_execution(filenames):
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    print(f"Многопроцессное выполнение заняло: {time.time() - start_time:.5f} секунд")


if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    linear_execution(filenames)

    parallel_execution(filenames)
