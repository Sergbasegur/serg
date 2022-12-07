# Задача 
# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Коэффициенты могут быть как положительными, так и отрицательными.
# Степени многочленов могут отличаться.
with open('file_1.txt', 'w', encoding='utf-8') as file:
    file.write('3*x^3 + 6*x^7')
with open('file_2.txt', 'w', encoding='utf-8') as file:
    file.write('10*x^5 + 8*x^4')

with open('file_1.txt','r') as file:
    mn_1 = file.readline()
    poligam_1 = mn_1.split()


with open('file_2.txt','r') as file:
    mn_2 = file.readline()
    poligam_2 = mn_2.split()

print(f'{poligam_1} + {poligam_2}')
sum_poly = poligam_1 + poligam_2

with open('sum_poligam.txt', 'w', encoding='utf-8') as file:
    file.write(f'{poligam_1} + {poligam_2}')