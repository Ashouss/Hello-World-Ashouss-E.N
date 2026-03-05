device_name = input("Введите название прибора: ")
inventory_number = input("Введите инвентарный номер: ")
is_working_input = input("Прибор исправен? (да/нет): ")
if is_working_input.upper() == "ДА":
    is_working = True
else:
    is_working = False

quantity = int(input("Введите количество: "))
print("\nНазвание\tИнв. номер\t Исправен\t Количество")
print("-" * 50)
print(f"{device_name}\t{inventory_number}\t{is_working}\t{quantity}")