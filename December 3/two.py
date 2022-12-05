with open('input.txt') as f:
    sacks = f.read().strip().split('\n')

points = 0
priorities = ".abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(0, len(sacks), 3):
    badge = list(set(sacks[i]) & set(sacks[i+1]) & set(sacks[i+2]))
    points += priorities.index(badge[0])

print(points)