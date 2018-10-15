#Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import sys

number = input("Введите число, содержавшее два или более знаков: ")

i = len(number)- 1
new_number = ""

while i>=0:
    new_number += number[i]
    i -= 1
print(new_number)

print(sys.getsizeof(i))
print(sys.getsizeof(number))
print(sys.getsizeof(new_number))

# При числе 96868684 = 14B для i
# 33B для number
# 33B для new_number
