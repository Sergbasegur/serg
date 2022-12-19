import json
import controller


path_to_db = 'basa_d.json'


def view_all_contact():

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    controller.user_controller()