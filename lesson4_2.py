# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 6 -> [2,3]
# 144 -> [2,3]

N = int(input("Введите число: "))
i = 2                                           # первое простое число
list = []
old = N
while i <= N:
    if N % i == 0:
        list.append(i)
        N //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} = {list}")