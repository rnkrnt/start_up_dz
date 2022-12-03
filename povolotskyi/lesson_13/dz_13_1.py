import random
from random_words import RandomWords

int_list = []
float_list = []
str_list = []


for i in range(5000):
    int_list.append(random.randint(0, 1000))
    float_list.append(round(random.uniform(0.1, 100.0), 1))
    str_list.append(RandomWords().random_word())

print(int_list)
print(float_list)
print(str_list)