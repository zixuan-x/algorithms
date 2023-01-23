from os import listdir

output_string_array = []

# 1. print table header:
header = '| #    | Title | Solution | Difficulty |\n| ---- | ----- | -------- | ---------- |\n'
output_string_array.append(header)

# 2. print table content:
# get all the file names in the leetcode directory
file_names = listdir('./leetcode')
question_lines = {}  # {number: line}

for file_name in file_names:
    if len(file_name.split('.')) < 3:
        continue
    number, title, extension = file_name.split('.')
    number, title = int(number), title.strip()
    blank, escaped_blank = ' ', '&#32;'
    # if extension == 'py':
    line = f"| {number} | {title} | [Python3](./leetcode/{number}.{escaped_blank}{escaped_blank.join(title.split(blank))}.py) |            |"
    question_lines[number] = line + '\n'

for number in sorted(question_lines):
    output_string_array.append(question_lines[number])

# 3. write result to a output.txy file
output_string = ''.join(output_string_array)
f = open('output.txt', 'w')
f.write(output_string)
f.close

print(len(file_names))