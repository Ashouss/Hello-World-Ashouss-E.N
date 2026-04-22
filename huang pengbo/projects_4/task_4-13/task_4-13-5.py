n = int(input("Введите количество чисел: "))

max_val = float(input("Введите число 1: "))

for i in range(2, n + 1):
    num = float(input(f"Введите число {i}: "))
    if num > max_val:
        max_val = num

print("Максимальное число:", max_val)