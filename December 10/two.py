with open("input.txt") as f:
    contents = f.read().strip().split("\n")

# Goal: create a dictionary with every cycle and the value of x
time_stamps = {}

current_cycle = 1
current_x = 1

# Create cycle-value dictionary
for line in contents:
    # noop instruction
    if "noop" in line:
        time_stamps[current_cycle] = current_x
        current_cycle += 1
        continue

    # add instruction
    if "addx" in line:
        # get value
        update = int(line.split(" ")[1])

        # start execution
        time_stamps[current_cycle] = current_x
        current_cycle += 1

        # second cycle
        time_stamps[current_cycle] = current_x
        current_cycle += 1

        # update x
        current_x += update

# create output image
crt_rows = []
current_row = ""
crt_index = 0

for cycle, value in time_stamps.items():
    # reset row
    if crt_index % 40 == 0:
        crt_rows.append(current_row)
        current_row = ""
        crt_index = 0

    # is cycle within sprite?
    if crt_index in [value - 1, value, value + 1]:
        current_row += "#"
    else:
        current_row += "."

    crt_index += 1

# add last row
crt_rows.append(current_row)

for row in crt_rows:
    print(row)
