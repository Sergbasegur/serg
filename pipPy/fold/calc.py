
# def main():
#     print('Калькулятор !!!')
    
#     while True:
#         # Выводим сообщение какие действия есть
#         print("Выберите действие которое хотите сделать:\n"
#               "Сложжение: +\n"
#               "Вычитание: -\n"
#               "Умножение: *\n"
#               "Деление: /\n"
#               "Выход: q\n")
#         # Переменная для хранения действия
#         number = input("Действие: ")
#         # Если action равен q то
#         if number == "q":
#             # Выводим сообщение
#             print("Выход из программы")
#             # Выходим из цикла
#             break
#         # Если action равен +, -, *, /, то
#         if number in ('+', '-', '*', '/'):
#             # Присваиваем значение переменной x
#             x = float(input("x = "))
#             # Присваиваем значение переменной y
#             y = float(input("y = "))
#             # Если action равен + то
#             if number == '+':
#                 # Выводим сумму x и y
#                 print('%.2f + %.2f = %.2f' % (x, y, x+y))
#             # Если action равен - то
#             elif number == '-':
#                 # Выводим разность x и y
#                 print('%.2f - %.2f = %.2f' % (x, y, x-y))
#             # Если action равен * то
#             elif number == '*':
#                 # Выводим результат умножения x на y
#                 print('%.2f * %.2f = %.2f' % (x, y, x*y))
#             # Если action равен / то
#             elif number == '/':
#                 # Если y не равен нулю то
#                 if y != 0:
#                     # Выводим результат деления x на y
#                     print('%.2f / %.2f = %.2f' % (x, y, x/y))
#                 else: # Иначе
#                     # Выводим сообщение, что на ноль делить нельзя
#                     print("Делить на ноль нельзя!!!")

# if __name__ == '__main__':
#     main()