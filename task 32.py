# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def random_list(a:int):
    b = list()
    for i in range(a):
        b.append(randint(-10,10))
    return b


def list_min_max(a, min_num, max_num):
    list_2 = list()
    for i in range(len(a)):
        if min_num <= a[i] <= max_num:
            list_2.append(i)
    return list_2

a= int(input("Введите длинну массива: "))

list_fist = random_list(a)
print(list_fist)


min_num = int(input("Введите минимальное число диапазона: "))
max_num= int(input("Введите максимальное число диапазона: "))

print(f"массив индексов чисел в заданном диапазоне {list_min_max(list_fist, min_num, max_num)}")


