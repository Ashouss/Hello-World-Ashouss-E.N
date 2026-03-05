medium_name = input("Введите название питательной среды: ")
agar_concentration = input("Введите концентрацию агара (%): ")
sterilization_temp = input("Введите температуру стерилизации (°C): ")

with open("recipe.txt", "w", encoding="utf-8") as card:
    card.write(f"{medium_name}\n")
    card.write(f"Концентрация агара: {agar_concentration}%\n")
    card.write(f"Температура стерилизации: {sterilization_temp}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")