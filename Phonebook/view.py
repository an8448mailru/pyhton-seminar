import csv

def choose_mode():
    return input('Введите дейсвие (1-добавление, 2-поиск): ')

def new_contact():
    name = input('Введите имя: ')
    phone_num = input('Введите номер телефона: ')
    return f'{name} || {phone_num}'

def show_found(result):
    print ('Результат поиска: ')
    for i in result:
        print(i)