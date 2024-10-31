file_names = ['1.txt', '2.txt', '3.txt']

files_with_line_numbers = []
for file_name in file_names:
    line_count = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            line_count += 1
    files_with_line_numbers.append((file_name, line_count))

sorted_files = sorted(files_with_line_numbers, key=lambda item: item[1])

with open('result.txt', 'w', encoding='utf-8') as file:
    for file_name, line_count in sorted_files:
        file.write(f"{file_name}\n{line_count}\n")
        with open(file_name, 'r', encoding='utf-8') as source_file:
            for line in source_file:
                file.write(line)
        file.write("\n")