# Задача
# Задайте натуральное число N.
#  Напишите программу, которая составит список
#  простых множителей числа N.
# Пример*
# - при N=236     ->        [2, 2, 59]

n = int(input("Введите число: "))
spisok = []
d = 2
m = n 
while d * d <= n:
        if n % d == 0:
            spisok.append(d)
            n//=d
        else:
            d += 1
spisok.append(n)
print('{} --> {}' .format(m, spisok))