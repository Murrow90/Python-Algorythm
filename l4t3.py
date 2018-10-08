# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125, ...
# Количество элементов (n) вводится с клавиатуры.

import time
import timeit
import cProfile

n = int(input("Введите число элементов: "))

f = 0
sum_n = 1
k = 1

while (n - 1) > f:
    sum_n += k / -2
    f = f + 1
    k = k / -2

print("Сумма равна", sum_n)

print(timeit.timeit())
cProfile.run('sum_n()') 


# для n = 100 timeit 0.0092945386278775
# cProfile        3 function calls in 0.000 seconds
#
#   Ordered by: standard name
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
