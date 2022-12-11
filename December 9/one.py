import math

with open("input.txt") as f:
    contents = f.read().split("\n")


def is_next_to(head, tail):
    """Generate adjacent squares from head and compare with tail"""
    adjacent_squares = [[x, y] for x in range(head[0] - 1, head[0] + 2) for y in range(head[1] - 1, head[1] + 2)]

    return tail in adjacent_squares


def update_tail(head, tail):
    """Make tail trail head."""

    # same row?
    if tail[1] == head[1]:
        # update tail column to get one step closer = the average
        return [(tail[0] + head[0]) // 2, tail[1]]

    # same column?
    if tail[0] == head[0]:
        return [tail[0], (tail[1] + head[1]) // 2]

    # diagonal
    edges = [[head[0], head[1] - 1], [head[0], head[1] + 1], [head[0] - 1, head[1]], [head[0] + 1, head[1]]]
    steps = [
        [tail[0] + 1, tail[1] + 1],
        [tail[0] + 1, tail[1] - 1],
        [tail[0] - 1, tail[1] + 1],
        [tail[0] - 1, tail[1] - 1],
    ]

    for step in steps:
        if step in edges:
            return step


def update_head(head, direction):
    if direction == "R":
        return [head[0] + 1, head[1]]
    if direction == "L":
        return [head[0] - 1, head[1]]
    if direction == "U":
        return [head[0], head[1] + 1]
    if direction == "D":
        return [head[0], head[1] - 1]


def print_board(head, tail, size):
    board_map = [["." for i in range(size)] for j in range(size)]

    # set 0, 0 as middle of board
    middle = math.ceil(size / 2)
    board_map[middle + tail[1]][middle + tail[0]] = "T"
    board_map[middle + head[1]][middle + head[0]] = "H"

    for row in board_map:
        print("".join(row))

    print()


def main():

    # parse instructions
    instructions = [line.split(" ") for line in contents]
    instructions = [(line[0], int(line[1])) for line in instructions]

    # define starting pos
    tail_positions = [(0, 0)]

    current_head = [0, 0]
    current_tail = [0, 0]

    # print_board(current_head, current_tail, 15)

    # loop
    for move in instructions:
        # update head one step at a time
        for _ in range(move[1]):
            current_head = update_head(current_head, move[0])

            # check if tail needs to be updated
            if not is_next_to(current_tail, current_head):

                current_tail = update_tail(current_head, current_tail)

                # add new position to list
                tail_positions.append((current_tail[0], current_tail[1]))

            # print_board(current_head, current_tail, 15)

    # turn into set
    print(len(set(tail_positions)))


if __name__ == "__main__":
    main()
