# 4. Задайте список из N элементов,
#  заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях.
#  Позиции вводятся с клавиатуры.

listt_s = []
N1 = int(input('Начало списка : '))
N2 = int(input('Конец списка : '))
for i in range(N1, N2 + 1):
    listt_s.append(i)
print(listt_s)

def number(listt_s):
    count = 0
    for x in listt_s:
        count +=1
    return count
print('Количество элементов в списке :',number(listt_s))

pos_1 = int(input('Введите позицию первого элемента :'))
pos_2 = int(input('Введите позицию второго элемента :'))

for i in range(len(listt_s)):
    proiz = listt_s[pos_1 - 1] * listt_s[pos_2 - 1]
print(proiz)




