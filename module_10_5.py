from time import time
from multiprocessing import Pool
def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()

files = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
# start_time = time()
# for file_name in files:
#     read_info(file_name)
# end_time = time()
# print(round(end_time - start_time, 4))

if __name__ == '__main__':
    start_time = time()
    with Pool() as pool:
        pool.map(read_info, files)
    end_time = time()
    print(round(end_time - start_time, 4))
