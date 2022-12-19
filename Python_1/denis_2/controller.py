import addContact as ac
import delete_contact as dc
import export_in_file as eif
import userBook as ui
def user_controller():

    num = ui.menu()
    if num < 0 or choice_num > 7:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif num == 0:
        ac.create()
    elif num == 1:
        ac.add()
    
    elif choice_num == 7:
        print('\nСпасибо что пользовались нашим приложением!\n\nДо новых встреч!')
        exit()

