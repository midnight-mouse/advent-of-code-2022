# Read file
with open("inventory.txt") as f:
    contents = f.read().strip().split('\n\n')

# Extract inventories and turn into ints
inventories = [line.split() for line in contents]
inventories = [list(map(int, i)) for i in inventories]

# Compute calories sums
calories = [sum(i) for i in inventories]

# Find max
max_calories = max(calories)
elf_number = calories.index(max_calories)

print(f'Elf number #{elf_number + 1} has the most with {max_calories} calories!')
