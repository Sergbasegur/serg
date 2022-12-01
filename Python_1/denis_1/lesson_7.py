# Задайте список из вещественных чисел.
#  Напишите программу, которая найдёт разницу между
#  максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

n = [1.1, 1.2, 3.1, 5, 10.01]
   
index_min = index_max = 0
value_min = value_max = n[0]


for i, a in enumerate(n[1:], 1):
    z = 0
    if a < value_min:
        value_min = a
        index_min = i
    if a > value_max:
        value_max = a
        index_max = i
z = n[index_max] - n[index_min] 
print(f'{n} --> {z}')
        