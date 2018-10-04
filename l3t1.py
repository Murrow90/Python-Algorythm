#В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

array = [i for i in range(2,100)]

f = 0
result = 0

while len(array) > f:
    b = 2
    while b <= 9:
        if array[f] % b == 0:
            result += 1
            break
        b += 1

    f += 1
    
print(result, "чисел кратны какому-либо в диапазоне от 2 до 9")
    
