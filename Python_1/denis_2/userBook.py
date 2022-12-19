import check
from export_in_file import export_txt


def start():
    greeting = 'Это твоя телефонная книга'

    print(f'{greeting}\n')


def menu():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    new_book = '0. Создать новую книгу или очистить существующую'
    addContact = '1. Добавить новый контакт'
    delete_contact = '2. Удалить контакт'
    view_all_contact = '3. Показать все контакты'
    export_to_file = '4. Экспортировать контакты в файл'
    to_exit = '5. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{new_contact}\n{delete_contact}\n{view_all_contact}\n{export_to_file}\n{to_exit}')
    return chek.digit_check()