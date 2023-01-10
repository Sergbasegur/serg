import logging
from bot import TOKEN
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, ConversationHandler)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

CHOICE, NUMBER_ONE, NUMBER_TWO, NUMBER_OPERATION, COMPLEX_1, COMPLEX_2, COMPLEX_OPERATION = range(7)

def start(update, _):
    update.message.reply_text(f'Привет, {update.effective_user.first_name}, это - калькулятор. Выберите пожалуйста команду.\n' 'Команда /cancel, чтобы прекратить разговор.\n\n')
    update.message.reply_text('1 - операции с числами;\n2 - операции с комплексными числами \n3 - Выйти из калькулятора \n')
    return CHOICE

def choice(update, context):
    user = update.message.from_user
    logger.info("Выбор операции: %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    if user_choice in '12':
        if user_choice == '1':
            update.message.reply_text('Введите первое число:\n ')
            return NUMBER_ONE
        if user_choice == '2':
            context.bot.send_message(update.effective_chat.id, 'Введите Re и Im первого числа через ПРОБЕЛ: ')
            return COMPLEX_1
        if user_choice == '3':
            update.message.reply_text('Спасибо, до свидания!')
            return ConversationHandler.END     
    else:
        update.message.reply_text('Ошибка ввода. Введите цифру операции: \n 1 - операции с числами;\n2 - для выхода \n')

def number_one(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_number = update.message.text
    if get_number.isdigit():
        get_number = float(get_number)
        context.user_data['number_one'] = get_number
        update.message.reply_text('Введите второе число')
        return NUMBER_TWO

    else:
        update.message.reply_text('Нужно ввести число')


def number_two(update, context):
    user = update.message.from_user
    logger.info("Пользователь ввел число: %s: %s", user.first_name, update.message.text)
    get_number = update.message.text
    if get_number.isdigit():
        get_number = float(get_number)
        context.user_data['number_two'] = get_number
        update.message.reply_text('Выберите действие: \n\n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n')
        return NUMBER_OPERATION

def complex_1(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь ввел число %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_1 = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_1'] = complex_1
        update.message.reply_text(f'Первое число {complex_1},  Введите Re и Im второго числа через ПРОБЕЛ: ')
        return COMPLEX_2
    else:
        update.message.reply_text('Ошибка. Введите Re и Im первого числа через ПРОБЕЛ')


def complex_2(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь ввел число %s: %s", user.first_name, update.message.text)
    user_choice = update.message.text
    test = user_choice.replace('-', '')
    if ' ' in test and (test.replace(' ', '')).isdigit():
        user_choice = user_choice.split(' ')
        complex_2 = complex(int(user_choice[0]), int(user_choice[1]))
        context.user_data['complex_2'] = complex_2
        update.message.reply_text(
            f'Второе число {complex_2}, Выберите действие: \n\n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n')
        return COMPLEX_OPERATION
    else:
        update.message.reply_text('Ошибка ввода. Введите Re и Im второго числа через ПРОБЕЛ')

def complex_operation(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    complex_1 = context.user_data.get('complex_1')
    complex_2 = context.user_data.get('complex_2')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = complex_1 + complex_2
        if user_choice == '-':
            result = complex_1 - complex_2
        if user_choice == '*':
            result = complex_1 * complex_2        
        if user_choice == '/':
            try:
                result = complex_1 / complex_2
            except:
                update.message.reply_text('Деление на ноль запрещено')
        update.message.reply_text(f'Результат: {complex_1} + {complex_2} = {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Ошибка ввода. \n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n')



def number_operation(update, context):
    user = update.message.from_user
    logger.info(
        "Пользователь выбрал операцию %s: %s", user.first_name, update.message.text)
    number_one = context.user_data.get('number_one')
    number_two = context.user_data.get('number_two')
    user_choice = update.message.text
    if user_choice in '+-/*':
        if user_choice == '+':
            result = number_one + number_two
        if user_choice == '-':
            result = number_one - number_two
        if user_choice == '*':
            result = number_one * number_two
        if user_choice == '/':
            try:
                result = number_one / number_two
            except:
                update.message.reply_text('Деление на ноль запрещено')
        update.message.reply_text(f'Результат: {number_one} {user_choice} {number_two} = {result}')
        return ConversationHandler.END
    else:
        update.message.reply_text('Ошибка ввода. Выберите действие: \n+ - для сложения; \n- - для вычетания; \n* - для умножения; \n/ - для деления. \n' )




def cancel(update, _):
    user = update.message.from_user
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    update.message.reply_text('Спасибо, до свидания!')
    return ConversationHandler.END


if __name__ == '__main__':
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(  
    
        entry_points=[CommandHandler('start', start)],
    
        states={
            CHOICE: [MessageHandler(Filters.text, choice)],
            NUMBER_ONE: [MessageHandler(Filters.text, number_one)],
            NUMBER_TWO: [MessageHandler(Filters.text, number_two)],
            NUMBER_OPERATION: [MessageHandler(Filters.text, number_operation)],
            COMPLEX_1: [MessageHandler(Filters.text, number_operation)],
            COMPLEX_2: [MessageHandler(Filters.text, number_operation)],
            COMPLEX_OPERATION: [MessageHandler(Filters.text, number_operation)]
          
        },
        fallbacks=[CommandHandler('cancel', cancel)],
    
        
    )

    dispatcher.add_handler(conversation_handler)
    print('server start')
    updater.start_polling()
    updater.idle()