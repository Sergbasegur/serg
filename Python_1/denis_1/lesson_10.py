# Задача 
# Вычислить число π c заданной точностью d
# Пример: 
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

from math import acos

def printValueOfPi():
    pi = round ( 2 * acos( 0.0 ), 3 )
    print (pi)
if __name__ == "__main__" :
    printValueOfPi()