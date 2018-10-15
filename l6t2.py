import sys
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

print(sys.getsizeof(array))
print(sys.getsizeof(i))
print(sys.getsizeof(array_ind))

# array = 192
# i = 28
# array_ind = 128
