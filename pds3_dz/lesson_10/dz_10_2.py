import sys

def create_list(num):
    new_num = None
    while not isinstance(new_num, int):
        try:
            new_num = int(input("Введите элемент списка: "))
        except ValueError as ex1:
            print(f"Ошибка {ex1}\nВведите целое число!", file=sys.stderr)
        except Exception as ex2:
            print(f"Ошибка {ex2}\nВведите целое число!", file=sys.stderr)
    my_list_1[num] = new_num


elem_list = 3
my_list_1 = [''] * elem_list
for num in range(elem_list):
    create_list(num)
my_list_2 = list(set(my_list_1))
if my_list_1 == my_list_2:
    print("Все элементы списка уникальны")
else:
    print("В списке присутствуют повторяющиесь элементы")