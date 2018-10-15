#Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
#Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import sys
import random

array = [random.randint(-10,15) for i in range(10)]
print(array)

i = 0
max_min = 0
number = 0


while len(array) > i:
    if array[i] < 0:
        if number == 0:
            number = array[i]
        if array[i] > number:
            number = array[i]
    i += 1

print("Наибольший отрицательный эллемент равен", number)

print(sys.getsizeof(array))
print(sys.getsizeof(i))            
print(sys.getsizeof(max_min))
print(sys.getsizeof(number))

# array = 100b
# i = 14b
# max_min = 12
# number = 14
