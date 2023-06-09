import os

while True:
    # Введення шляху до файлу
    file_path = input("Enter the path to the file: ")

    if not os.path.exists(file_path):
        # Перевірка, чи файл існує
        print("File not found!")
        continue

    with open(file_path, 'r') as file:
        # Зчитування вмісту файлу
        content = file.readlines()

    # Обчислення загальної кількості рядків
    total_lines = len(content)
    # Обчислення кількості порожніх рядків
    empty_lines = content.count('\n')
    # Обчислення кількості рядків, що містять символ "c"
    lines_with_c = sum('c' in line for line in content)
    # Обчислення загальної кількості входжень символу "c"
    c_count = sum(line.count('c') for line in content)
    # Обчислення кількості рядків, що містять слово "dust"
    lines_with_dust = sum('dust' in line for line in content)

    # Виведення результатів аналізу файлу
    print(f"\nFile: {file_path}")
    print(f"total lines: {total_lines}")
    print(f"empty lines: {empty_lines}")
    print(f"lines with \"c\": {lines_with_c}")
    print(f"\"c\" count: {c_count}")
    print(f"lines with \"dust\": {lines_with_dust}")

    # Запит на аналіз іншого файлу
    answer = input("Do you want to analyze another file? (+/-): ")
    if answer.lower() != '+':
        break
