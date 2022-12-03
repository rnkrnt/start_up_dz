import random
from random_words import RandomWords
import  time
from statistics import mean

int_list = []
float_list = []
str_list = []

for i in range(5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(round(random.uniform(0.1, 100.0), 1))
    str_list.append(RandomWords().random_word())

def selection_sort(data):
    for scanIndex in range(0, len(data)):
        minIndex = scanIndex
        for compIndex in range(scanIndex + 1, len(data)):
            if data[compIndex] < data[minIndex]:
                minIndex = compIndex
        if minIndex != scanIndex:
            data[scanIndex], data[minIndex] = data[minIndex], data[scanIndex]

def time_count(data, iter):
    aver_time = []
    for i in range(iter):
        start = time.time()
        selection_sort(data)
        large = time.time() - start
        aver_time.append(large)
        print("Finished iterration: " + str(i + 1))
    average = mean(aver_time)
    return average

repeat = 3
data_sort = int_list
rezult = time_count(data_sort, repeat)
print(rezult)



# copy_my_list = my_list
# cur_time = time.time()
# selection_sort(copy_my_list)
# print(f"Duration time: {time.time() - cur_time}")