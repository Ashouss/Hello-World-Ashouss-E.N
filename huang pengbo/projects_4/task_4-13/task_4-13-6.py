n = int(input("Введите N: "))

sum_sq = 0
for i in range(1, n + 1):
    sum_sq = sum_sq + i * i

print("Сумма квадратов:", sum_sq)