import addContact as ac
import exportFile as f
import userBook as ui
def user_controller():

    num = ui.menu()
    if num < 0 or choice_num > 7:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_controller()
    elif num == 1:
        ac.create()
    elif num == 2:
        ac.add()
    elif num == 3:
        f.export_txt()
    
    
    elif num == 0:
        print('\nСпасибо что пользовались нашим приложением!\n\nДо новых встреч!')
        exit()

