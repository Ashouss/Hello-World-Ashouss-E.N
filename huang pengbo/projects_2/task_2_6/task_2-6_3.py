print(f"Донор: {donor}, Пациент: {patient}")
if donor == patient:
    print("Группа совпадает — переливание возможно")
elif donor == "0":
    print("Донор с группой 0 — переливание возможно")
else:
    print("Переливание невозможно")