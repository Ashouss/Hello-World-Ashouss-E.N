arr = list(map(float, input("Введите числа через пробел: ").split()))

if len(arr) == 0:
    avg = 0
else:
    avg = sum(arr) / len(arr)

print("Среднее арифметическое массива:", avg)