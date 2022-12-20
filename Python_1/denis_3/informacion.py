import childrenInfo as chi
import schoolCabinet as sCab


def sistemSchool():
    print("\nЭто информационная система успеваемости детей в школе")
    num = int(input('Введите номер поиска: \n \
    1: Поиск ID школьника по фамилии \n \
    2: Посмотреть класс  и ряд которое занимает школьник \n \
    3: Выход\n \
    Вы ввели: '))

    if num == 1:
        surnam = str(input("Введите фамилию ученика: "))
        if surnam in chi.children_id['Фамилия']:
            index = chi.children_id['Фамилия'].index(surnam)
        print(f"{chi.children_id['ID'][index]}, {chi.children_id['Имя'][index]},{chi.children_id['Фамилия'][index]},{chi.children_id['Дата рождения'][index]}, {chi.children_id['Успеваемость'][index]}")
        print('\nХотите выполнить какую-то другую операцию??? Y или N: ')
        num = input()
        if num == 'Y' or 'y' or 'У' or 'у':
            sistemSchool()
        exit()

    elif num == 2:
        c = input('Введите ID школьника для вывода по классам: ')
        if c in sCab.class_id['ID']:
            index = sCab.class_id['ID'].index(c)
            print(f" Сидит в классе - {sCab.class_id['Предмет'][index]}\n\, номер класса - {sCab.class_id[index]}, это {sCab.class_id['Ряд в классе'][index]}, Имя: {chi.children_id['Имя'][index]}, Фамилия - {chi.children_id['Фамилия'][index]}, Успеваемость у школьника: {chi.children_id['Успеваемость'][index]}")
            print('\nХотите выполнить другую операцию??? Y или N: ')
            num = input()
            if num == 'Y' or 'y' or 'У' or 'у':
                sistemSchool()
            exit()
    else:
        print('повторите')
    exit()


sistemSchool()