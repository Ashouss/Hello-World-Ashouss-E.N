TOTAL_WIDTH = 42

prompts = {"fio": len(" ФИО исследователя : "),"date": len(" Дата : "),"exp": len(" Эксперимент : "),"conclusion": len(" Вывод: ")}

with open("journal_perfect.txt", "w", encoding="utf-8") as j:

    j.write("+" + "-" * (TOTAL_WIDTH - 2) + "+\n")

    title = "Электронный лабораторный журнал"
    padding = TOTAL_WIDTH - 4 - len(title)
    left_pad = padding // 2
    right_pad = padding - left_pad
    j.write("| " + " " * left_pad + title + " " * right_pad + " |\n")

    j.write("|" + "-" * (TOTAL_WIDTH - 2) + "|\n")

    content_width = TOTAL_WIDTH - prompts["fio"] - 2 
    j.write(f"| ФИО исследователя : {researcher.ljust(content_width)}|\n")

    content_width = TOTAL_WIDTH - prompts["date"] - 2
    j.write(f"| Дата : {date.ljust(content_width)}|\n")

    content_width = TOTAL_WIDTH - prompts["exp"] - 2
    j.write(f"| Эксперимент : {experiment.ljust(content_width)}|\n")
    j.write("|" + "-" * (TOTAL_WIDTH - 2) + "|\n")
    j.write("| Вывод:".ljust(TOTAL_WIDTH - 1) + "|\n")

    content_width = TOTAL_WIDTH - 4 
    j.write(f"| {conclusion.ljust(content_width)} |\n")
    j.write("+" + "-" * (TOTAL_WIDTH - 2) + "+\n")