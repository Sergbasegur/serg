# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

def number_l(list_s):

    l = len(list_s)//2 + 1 if len(list_s) % 2 != 0 else len(list_s)//2
    new_lst = [list_s[i]*list_s[len(list_s)-i-1] for i in range(l)]
    print(new_lst)


list_s = []
number_l(list_s)
list_s = list(map(int, input("Введите числа через пробел:\n").split()))
number_l(list_s)