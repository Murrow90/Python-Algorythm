print("Введите координаты точки A")

x1 = int(input("x1 = "))
y1 = int(input("y1 = "))

print("Введите координаты точки B")

x2 = int(input("x2 = "))
y2 = int(input("y2 = "))

A = y1 - y2
B = x2 - x1
C = (x1 * y2) - (x2 * y1)

if B >= 0 and C >= 0:
    print(str(A) + "x" + "+" + str(B) + "y" + "+" + str(C) + " = 0")

elif B < 0 and C >= 0:
    print(str(A) + "x" + str(B) + "y" + "+" + str(C) + " = 0")

elif B >= 0 and C < 0:
     print(str(A) + "x" + "+" + str(B) + "y" + str(C) + " = 0")

else:
    print(str(A) + "x" + str(B) + "y" + str(C) + " = 0")
