# Задача
# Напишите программу, удаляющую из файла все слова, 
# содержащие "абв"

#with open('den.txt', 'w', encoding='utf-8') as file:
 #   file.write('абв уак абв укен ыясаа абв')
    #lines = file.readline()
    #lines = file.split()

file = ('abv wer tre abv qwe sre abv abv')


slovo = ('abv')
for string in file.split('\n'):
    for i in slovo:
        string = string.replace(i, '')
    if string:
        print(string)












