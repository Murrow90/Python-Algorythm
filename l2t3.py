# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

number = input("Введите число, содержавшее две или более знаков: ")

i = len(number)- 1
new_number = ""

while i>=0:
    new_number += number[i]
    i -= 1
print(new_number)
