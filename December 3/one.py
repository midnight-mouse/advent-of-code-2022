with open('input.txt') as f:
    rucksacks = f.read().split('\n')

# Find common items by doing set and
commons = [list(set(sack[:len(sack)//2]) & set(sack[len(sack)//2:])) for sack in rucksacks]

# Sum scores
priorities = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
scores = sum([priorities.index(item[0]) for item in commons])

print(scores)