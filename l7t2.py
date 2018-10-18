#Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). 
#Выведите на экран исходный и отсортированный массивы.

#Честно признаюсь, этот алгоритм не работает. Но поскольку я так и не смогла разобраться на каком этапе все пошло не так, сдаю его в таком виде.
import random

n = random.randint(10,50)

print(n)

array = [random.randint(1,50) for i in range(n)]
array1 = []
array2 = []
new_array = []

print(array)

i = int(len(array) / 2)
print(i)
array1 = array[:i]
i = i + 1
array2 = array[i:-1]

print(array1)
print(array2)

f = 0
n = 0
g = 0
m = 0 

while len(array1) > f:
    while len(array2) > f:
        if array1[n] < array2[g]:
            m = array1[n]
            new_array.append(m)
            n += 1

        else:
            m = array2[g]
            new_array.append(array2[g])
            g +=1

        f += 1

print(new_array)
