arr = list(map(int, input("Введите числа через пробел: ").split()))

sum_odd = 0
for num in arr:
    if num % 2 != 0:
        sum_odd = sum_odd + num

print("Сумма нечётных элементов:", sum_odd)