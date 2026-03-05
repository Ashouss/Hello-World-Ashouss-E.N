total_capsules = int(input("Введите общее количество произведенных капсул: "))
package_capacity = int(input("Введите количество капсул в одной упаковке: "))

full_packages = total_capsules // package_capacity
remaining = total_capsules % package_capacity

print("\n--- Отчет фасовочного цеха ---")
print(f"Полных упаковок: {full_packages}")
print(f"Остаток капсул: {remaining}")