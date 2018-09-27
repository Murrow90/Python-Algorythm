import random
import string

x1 = int(input("Введите начало ряда:"))
x2 = int(input("Введите конец ряда:"))

digit = random.randint(x1, x2)
decimal = random.uniform(x1, x2)

a = input("Введите первую букву:")
z = input("Введите последнюю букву:")

letter = random.choice(z)
print(letter)
