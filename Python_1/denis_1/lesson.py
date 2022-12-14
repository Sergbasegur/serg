# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр

vech = float(input('введите вещественное число - '))

while vech != int(vech):
    vech *= 10
sum = 0
# per = 1
while vech > 0:
    d = vech % 10
    sum += d
    vech //=10
    
print(sum)






