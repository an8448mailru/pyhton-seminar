# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).

x = int(input('Введите число x≠0:'))
y = int(input('Введите число y≠0:'))

if x == 0 and y == 0:
    print('Введите другие координаты, x≠0 y≠0')
elif x > 0 and y > 0:
    print(
        f'Точка находится в 1 плоскости')
elif x < 0 and y > 0:
    print(
        f'Точка находится во 2 плоскости')
elif x < 0 and y < 0:
    print(
        f'Точка находится в 3 плоскости')
elif x > 0 and y < 0:
    print(
        f'Точка находится в 4 плоскости')