import check
from exportFile import export_txt


def start():
    book = 'Это твоя телефонная книга'

    print(f'{book}\n')


def menu():
    what_to_do = 'Выберите соответствующую цифру в меню:'
    to_exit = '0. Выход'
    addContact = '1. Создать новый справочник'
    create_contact= '2. Добавить новый контакт'
    exportFile = '3. Экспортировать контакты в файл'
    delete_contact = '4. Удалить контакт'

    view_all_contact = '5. Показать все контакты'
   
    
    print(f'{what_to_do}\n{to_exit}\n{addContact}\n{create_contact}\n{exportFile}\n{delete_contact}\n{view_all_contact}')
    return check.number_check()