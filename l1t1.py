number = input("Введите трехзначное число: ")

if len(number) == 3:
    x = int(number[0])
    y = int(number[1])
    z = int(number[2])
    S = x + y + z
    P = x * y * z
    print("Сумма равна", S)
    print("Произведение равно", P)
else:
    print("Это не трехзначное число")
