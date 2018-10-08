#Во втором массиве сохранить индексы четных элементов первого массива.
#Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 0, 3, 4, 5 (индексация начинается с нуля),
#т.к. именно в этих позициях первого массива стоят четные числа.

import time
import timeit
import cProfile
import random


array = [random.randint(1,100) for i in range(10)]
print(array)

array_ind = []
i = 0

while len(array) > i:
    if array[i] % 2 == 0:
        array_ind.append(i)
    i += 1

print(array_ind)

print(timeit.timeit())
cProfile.run('array_ind(10)')
    
#для timeit 0.008186337828689147

#для cProfile везде одинаковый результат, кажется, я делаю что-то неправильно:
#3 function calls in 0.000 seconds

#   Ordered by: standard name

#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
