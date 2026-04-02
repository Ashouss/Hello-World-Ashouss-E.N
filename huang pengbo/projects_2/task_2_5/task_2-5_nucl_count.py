print("=== Анализ последовательности ДНК ===\n")

dna = input("Введите последовательность ДНК: ")

dna_upper = dna.upper()
print(f"\nПоследовательность в верхнем регистре: {dna_upper}")

total = len(dna_upper)
a = dna_upper.count("A")
t = dna_upper.count("T")
g = dna_upper.count("G")
c = dna_upper.count("C")

print("\nПодсчёт нуклеотидов:")
print(f"A: {a}")
print(f"T: {t}")
print(f"G: {g}")
print(f"C: {c}")

print(f"\nОбщая длина: {total} нуклеотидов")