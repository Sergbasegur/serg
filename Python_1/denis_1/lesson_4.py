# 5. Реализуйте алгоритм перемешивания списка.
# Из библиотеки random использовать можно только randint

import random
list_s = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list_s)

for i in range(len(list_s) - 1, 0, -1):

    x = random.randint(0, i + 1)

    list_s[i], list_s[x] = list_s[x], list_s[i]

print(str(list_s))