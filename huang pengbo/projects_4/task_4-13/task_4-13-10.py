arr = list(map(float, input("Введите числа через пробел: ").split()))

sum_odd_index = 0
for i in range(len(arr)):
    if i % 2 != 0:
        sum_odd_index = sum_odd_index + arr[i]

print("Сумма элементов с нечётными индексами:", sum_odd_index)