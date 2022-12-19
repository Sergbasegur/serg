import json
import controller


bd = 'basa_d.json'


def view_all_contact():

    with open(bd, 'r', encoding='utf-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            print(data[i])
    controller.user_controller()