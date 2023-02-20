import sys

def my_function(month_num):
    month_list = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
    try:
        rez = month_list[month_num - 1]
    except Exception as ex1:
        print(f"Ошибка {ex1}\n", file=sys.stderr)
        return None
    return rez


def enter_num():
    x = "string"
    print("Введите номер месяца: ")
    while not isinstance(x, int):
        try:
            x = int(input())
        except Exception as ex2:
            print(f"Ошибка {ex2}\nВведите целое число.", file=sys.stderr)
        return x

rezult =  None
while rezult == None:
    x = enter_num()
    rezult = my_function(x)

print(rezult)