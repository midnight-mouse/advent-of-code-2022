import math


def get_adjacent_squares(pos):
    return [[x, y] for x in range(pos[0] - 1, pos[0] + 2) for y in range(pos[1] - 1, pos[1] + 2)]


def is_next_to(head, tail):
    """Generate adjacent squares from head and compare with tail"""

    return tail in get_adjacent_squares(head)


def update_tail(head, tail):
    """Make tail trail head."""

    # same row?
    if tail[1] == head[1]:
        # update tail column to get one step closer = the average
        newTail = [(tail[0] + head[0]) // 2, tail[1]]

    # same column?
    elif tail[0] == head[0]:
        newTail = [tail[0], (tail[1] + head[1]) // 2]

    # diagonal
    else:
        edges = get_adjacent_squares(head)
        steps = [
            [tail[0] + 1, tail[1] + 1],
            [tail[0] + 1, tail[1] - 1],
            [tail[0] - 1, tail[1] + 1],
            [tail[0] - 1, tail[1] - 1],
        ]

        for step in steps:
            if step in edges:
                newTail = step

    if newTail == None:
        print("NONE!")
    else:
        return newTail


def update_head(head, direction):
    if direction == "R":
        return [head[0] + 1, head[1]]
    if direction == "L":
        return [head[0] - 1, head[1]]
    if direction == "U":
        return [head[0], head[1] - 1]
    if direction == "D":
        return [head[0], head[1] + 1]


def print_board(positions, size):
    board_map = [["." for i in range(size)] for j in range(size)]

    # set 0, 0 as middle of board
    middle = math.ceil(size / 2)
    for i in range(len(positions) - 1, -1, -1):
        if i == 0:
            board_map[middle + positions[i][1]][middle + positions[i][0]] = "H"
        else:
            board_map[middle + positions[i][1]][middle + positions[i][0]] = f"{i}"

    for row in board_map:
        print("".join(row))

    print()


def print_trace(track, size):
    board_map = [["." for i in range(size)] for j in range(size)]
    middle = math.ceil(size / 2)

    for pos in track:
        board_map[middle + pos[1]][middle + pos[0]] = "#"

    board_map[middle][middle] = "s"
    for row in board_map:
        print("".join(row))

    print()


def main():

    with open("input.txt") as f:
        contents = f.read().split("\n")

    # parse instructions
    instructions = [line.split(" ") for line in contents]
    instructions = [(line[0], int(line[1])) for line in instructions]

    # define starting pos
    positions = [[0, 0] for i in range(10)]
    track = [(0, 0)]

    # print_board(current_head, current_tail, 15)

    # loop
    for move in instructions:
        # update head one step at a time
        for _ in range(move[1]):
            positions[0] = update_head(positions[0], move[0])

            # go through all the tails
            for i in range(1, len(positions)):
                if not is_next_to(positions[i - 1], positions[i]):

                    positions[i] = update_tail(positions[i - 1], positions[i])

                    # add new position to list
                    if i == len(positions) - 1:
                        track.append((positions[i][0], positions[i][1]))

            # print_board(positions, 40)

    # turn into set
    # print_trace(track, 40)
    print(len(set(track)))


if __name__ == "__main__":
    main()
