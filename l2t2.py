# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

number = input("Введите число более трех знаков: ")

i = 0
odd = 0
even = 0

while i != len(number):
    if int(number[i]) % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1
    i += 1
print("Число четных цифр", even, "число нечетных -", odd)
