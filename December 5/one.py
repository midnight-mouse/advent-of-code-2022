import re

with open('input.txt') as f:
    crates_str, instructions = f.read().split('\n\n')

# extract number of crates
crate_num = int(crates_str[-2])

# extract crates
crates = [[] for i in range(crate_num + 1)]

for row in crates_str.split("\n")[:-1]:
    for index, column in zip(range(1, len(row), 4), range(1, crate_num + 1)):
        crate = row[index]
        if crate != ' ': crates[column].append(crate)

# the last crate is on top
crates = [list(reversed(crate)) for crate in crates]

# perform instructions
for instruction in instructions.split("\n"):
    # Extract values
    amount, A, B  = [int(item) for item in re.findall(r'\d+', instruction)]
    
    # Move the uppermost crate to the next stack
    for i in range(amount):
        crates[B].append(crates[A].pop())

# Get top crates
top = ''.join([crate[-1] for crate in crates[1:]]).strip()
print(top)