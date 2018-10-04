#В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

array = [random.randint(1,100) for i in range(10)]
print(array)

i = 0
i_min = 0
i_max = 0

m = min(array)


while len(array) > i:
    if array[i] == m:
        i_min = i
    i += 1

mx = max(array)


f = 0

while len(array) > f:
    if array[f] == mx:
        i_max = f
    f += 1

array[i_min] = mx
array[i_max] = m

print(mx, m)
print(array)
