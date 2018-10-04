#Определить, какое число в массиве встречается чаще всего.
import random

array = [random.randint(1,10) for i in range(50)]
print(array)

            
frq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
i = 0


while len(array) > i:
    frq[array[i]] = frq[array[i]] + 1
    i += 1

max_frq = max(frq)


i = 0
final = 0

while len(frq) > i:
    if frq[i] == max_frq:
        final = i
    i += 1


print("Наиболее частое число в списке", final)
