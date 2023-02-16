# Задача 30: Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
#  Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


def input_num():
    return int(input("Введите число: "))

def arithmetic_progression(a,b,c):
    list_arith= list()
    for i in range(c):
        list_arith.append(a)
        a+=b
    return list_arith

# def arithmetic_progression2(a,b,c):
#     list_arith= list()
#     for i in range(1, c):
#         list_arith.append(a+(i-1)*b)
#     return list_arith


fist_num = input_num()
dif_num = input_num()
coin_list = input_num()

print(arithmetic_progression(fist_num, dif_num, coin_list))
