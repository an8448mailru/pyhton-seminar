# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным.

number = int(input("Введите номер дня недели от 1 до 7, где 1 это ПН, а 7 это ВС: "))

if number < 1 or number > 7:
    print('Это неверное число)')
elif number > 5:
    print('Это выходной день.')
else:
    print('Это рабочий день.')