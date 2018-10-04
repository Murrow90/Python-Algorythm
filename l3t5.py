#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

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
            
