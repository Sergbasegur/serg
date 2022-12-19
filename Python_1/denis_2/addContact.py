import json
import controller


def create():
    json_data = []
    with open('basa_d.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
    controller.user_controller()


def add():
    name = input("Введите имя: ")
    surname = input('Введите Фамилию: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите коментарий: ')
    base_data = {
        "Name": name,
        "Surname": surname,
        "Phone number": phone,
        "Comment": comment,
    }
    data = json.load(open("basa_d.json"))
    data.append(base_data)
    with open("basa_d.json", "w", encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)
    print('\nКонтакт успешно добавлен\n')
    controller.user_controller()