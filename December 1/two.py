inventory_file = "inventory.txt"

# Read file
with open(inventory_file) as f:
    contents = f.read().strip().split('\n\n')

# Extract inventories and turn into ints
inventories = [line.split() for line in contents]
inventories = [list(map(int, i)) for i in inventories]

# Compute calories sums
calories = [sum(i) for i in inventories]

# Find top three
top_cals = []

for i in range(3):
    max_calories = max(calories)
    elf_number = calories.index(max_calories)

    # add to top cals, remove from calories
    top_cals.append((elf_number, max_calories))
    del calories[elf_number]

# Find sum
top_sum = sum([i[1] for i in top_cals])

print(f'The top three elves have {top_sum} calories together!')
