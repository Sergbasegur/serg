def number_check():
    try:
        input_number = int(input('Введите число: \n'))
        return input_number
    except ValueError:
        print('Это должно быть число\n')
        return number_check()