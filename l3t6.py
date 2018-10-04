#В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
#Сами минимальный и максимальный элементы в сумму не включать.

#Я че-то не очень поняла, по позиции или по значению должны они быть заключены между минимальным и максимальным поэтому сделала для обоих кейсов.
#По позиции:
import random

array = [random.randint(1,100) for i in range(10)]
print(array)

min_i = min(array)
max_i = max(array)
print(min_i, max_i)

i = 0
sum_num = 0

while len(array) > i:
    if array[i] == max_i:
        max_i = i
    i += 1
print(max_i)

i=0

while len(array) > i:
    if array[i] == min_i:
        min_i = i
    i += 1
print(min_i)

i=0
while len(array) > i:
    if min_i < max_i:
        if i > min_i:
            if i < max_i:
                sum_num = sum_num + array[i]
    else:
        if i < min_i:
            if i > max_i:
                sum_num = sum_num + array[i]
    i += 1

print("Сумма равна", sum_num)

#ПО значению:

array = [random.randint(1,100) for i in range(10)]
print(array)

min_i = min(array)
max_i = max(array)
print(min_i, max_i)

i = 0
sum_num = 0

while len(array) > i:
    if array[i] != min_i:
        if array[i] != max_i:
            sum_num = sum_num + array[i]
    i += 1

print("Сумма равна", sum_num)
