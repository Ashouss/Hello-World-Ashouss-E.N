arr = list(map(float, input("Введите числа через пробел: ").split()))

sum_even_index = 0
count_even_index = 0

for i in range(len(arr)):
    if i % 2 == 0:
        sum_even_index = sum_even_index + arr[i]
        count_even_index = count_even_index + 1

if count_even_index > 0:
    avg = sum_even_index / count_even_index
else:
    avg = 0

print("Среднее арифметическое элементов с чётными индексами:", avg)