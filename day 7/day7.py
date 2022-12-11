input_file = [line.split(' ') for line in open("input.txt").read().strip().split('\n')]

max_size = 100000
folder_stack = []
sizes = {}

for line in input_file:
    if line[0] == '$' and line[1] == 'cd':
        if line[2] == '..':
            folder_stack.pop()
        else:
            folder_stack.append(line[2])
    elif line[0].isnumeric():
        for folder in folder_stack:
            if folder not in sizes:
                sizes[folder] = int(line[0])
            else :
                sizes[folder] += int(line[0])
        # print(sizes)

# print(sizes)
print(sum([sizes[folder] for folder in sizes if sizes[folder]<=max_size]))