import os

while True:
    file_path = input("Enter the path to the file: ")

    if not os.path.exists(file_path):
        print("File not found!")
        continue

    with open(file_path, 'r') as file:
        content = file.readlines()

    
    total_lines = len(content)
    empty_lines = content.count('\n')
    lines_with_c = sum('c' in line for line in content)
    c_count = sum(line.count('c') for line in content)
    lines_with_dust = sum('dust' in line for line in content)

    print(f"\nFile: {file_path}")
    print(f"total lines: {total_lines}")
    print(f"empty lines: {empty_lines}")
    print(f"lines with \"c\": {lines_with_c}")
    print(f"\"c\" count: {c_count}")
    print(f"lines with \"dust\": {lines_with_dust}")

    answer = input("Do you want to analyze another file? (+/-): ")
    if answer.lower() != '+':
        break
