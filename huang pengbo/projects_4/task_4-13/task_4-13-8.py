arr = list(map(float, input("Введите числа через пробел: ").split()))

count = 0
for num in arr:
    if num > 0:
        count = count + 1

print("Количество положительных чисел:", count)