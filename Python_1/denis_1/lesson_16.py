# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

from random import randint

def input_sum(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def value_n_k_c_v(name, k, counter, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

play_1 = input("Введите имя первого игрока: ")
play_2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
flag = randint(0,2) # флаг очередности
if flag:
    print(f"Первый ходит {play_1}")
else:
    print(f"Первый ходит {play_2}")

counter1 = 0 
counter2 = 0

while value > 28:
    if flag:
        k = input_sum(play_1)
        counter1 += k
        value -= k
        flag = False
        value_n_k_c_v(play_1, k, counter1, value)
    else:
        k = input_sum(play_2)
        counter2 += k
        value -= k
        flag = True
        value_n_k_c_v(play_2, k, counter2, value)

if flag:
    print(f"Выиграл {play_1}")
else:
    print(f"Выиграл {play_2}")