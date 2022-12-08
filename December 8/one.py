with open("input.txt") as f:
    contents = f.read().strip().split("\n")


def is_visible(tree_map, row, col):
    def visible_check(subset):
        # All trees must be less in height
        if False not in [item < tree_map[row][col] for item in subset]:
            return True
        else:
            return False

    # Check right, left, up, and down
    if visible_check(tree_map[row][col + 1 :]):  # right
        return True
    if visible_check(tree_map[row][:col]):  # left
        return True
    if visible_check([patch[col] for patch in tree_map][:row]):  # up
        return True
    if visible_check([patch[col] for patch in tree_map][row + 1 :]):  # down
        return True

    return False


# Turn into 2D list of ints
tree_map = [list(row) for row in contents]
tree_map = [list(map(int, i)) for i in tree_map]

# go through every row and column in middle
edge_vis = 2 * len(tree_map[0]) + 2 * (len(tree_map) - 2)
middle_vis = sum(
    [is_visible(tree_map, row, col) for row in range(1, len(tree_map) - 1) for col in range(1, len(tree_map[0]) - 1)]
)

tot_vis = edge_vis + middle_vis
print(tot_vis)
