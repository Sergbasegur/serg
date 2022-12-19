import json
import controller


path_to_db = 'basa_d.json'


def delete_contact():
    name = input('Введите имя или фамилию контакта, которого надо удалить:  ')

    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
        if name not in data:
                 print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)
    print('\nКонтакт удалён!\n')
    controller.user_controller()