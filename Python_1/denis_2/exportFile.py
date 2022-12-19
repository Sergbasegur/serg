import json
import controller
path_to_db = 'basa_d.json'


def export_txt():
    name = input('Введите имя или фамилию контакта, для экспорта в файл:  ')

    with open(path_to_db, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                with open('exp_contact.txt', 'a', encoding='utf-8') as export:
                    export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
                        data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

    print('\nКонтакты успешно экспортированы в файл!\n')
    controller.user_controller()
