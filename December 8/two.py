with open("input.txt") as f:
    contents = f.read().strip().split("\n")


def get_scenic_score(tree_map, row, col):
    subtrees = [
        tree_map[row][col + 1 :],  # right
        list(reversed(tree_map[row][:col])),  # left
        list(reversed([patch[col] for patch in tree_map][:row])),  # up
        [patch[col] for patch in tree_map][row + 1 :],  # down
    ]

    score = 1

    for trees in subtrees:
        count = 0
        for tree in trees:
            count += 1
            if tree >= tree_map[row][col]:
                break

        score *= count

    return score


# Turn into 2D list of ints
tree_map = [list(row) for row in contents]
tree_map = [list(map(int, i)) for i in tree_map]

coordinates = [(row, col) for row in range(len(tree_map)) for col in range(len(tree_map[0]))]
scores = [get_scenic_score(tree_map, row, col) for row, col in coordinates]

print(max(scores))
