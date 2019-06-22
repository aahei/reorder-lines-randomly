from random import randint

file_name = 'vocabulary.txt'
output_file_name = 'reordered-vocabulary.txt'

with open(file_name) as file_object:
    lines = []
    for line in file_object:
        if line.isspace():
            continue # In the given file(vocabulary.txt), it contains empty lines
        lines.append(line.rstrip())
    with open(output_file_name, 'w') as output_file:
        for i in range(len(lines), 1, -1): # To count from bigger number to smaller number
            random_line = randint(1, i) # So that the random index can be chosen from remaining elements
            output_file.write(lines[random_line-1] + '\n')
            del lines[random_line-1]
