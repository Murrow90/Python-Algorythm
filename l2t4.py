# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input("Введите число элементов: "))

f = 0
sum_n = 1
k = 1

while (n - 1) > f:
    sum_n += k / -2
    f = f + 1
    k = k / -2

print("Сумма равна", sum_n)