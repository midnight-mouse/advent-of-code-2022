with open('input.txt') as f:
    games = f.read().split('\n')

# Create move-point chart
moves = { letter: 'ACBXZY'.index(letter) % 3 + 1 for letter in 'ACBXZY' }

points = 0
for game in games:
    opponent, you = game.split(' ')
    points += 'ABCXYZ'.index(you) % 3 + 1

    # tie
    if moves[opponent] == moves[you]:
        points += 3
    # win
    elif (moves[you]) % 3 == (moves[opponent] - 1):
        points += 6

print(f'Total: {points}')
