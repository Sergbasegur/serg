# Задача
# Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен
#  степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
max_v=100
k = int(input('Введите натуральную степень k:'))

ratio=[randint(0,max_v) for i in range(k)]+[randint(1,max_v)]
polynominal='+'.join([f'{(j,"")[j==1]}x^{i}' for i, j in enumerate(ratio) if j][::-1])

polynominal=polynominal.replace('x^1+', 'x+')
polynominal=polynominal.replace('x^0', '')
polynominal+=('','1')[polynominal[-1]=='+']
polynominal=(polynominal, polynominal[:-2])[polynominal[-2:]=='^1']
print(polynominal)