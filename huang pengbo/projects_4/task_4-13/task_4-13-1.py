a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = float(input("Введите число d: "))

min_val = a
if b < min_val:
    min_val = b
if c < min_val:
    min_val = c
if d < min_val:
    min_val = d

print("Минимальное число:", min_val)