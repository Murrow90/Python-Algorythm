#В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import time
import timeit
import cProfile
import random

array = [random.randint(-10,500) for i in range(1000)]
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


print(timeit.timeit())
cProfile.run('number()')            

# для timeit: 0.008713063591846813

# для cProfile:
#3 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
