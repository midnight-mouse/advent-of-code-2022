with open("input.txt") as f:
    contents = f.read().strip().split("\n")

# Goal: create a dictionary with every cycle and the value of x
time_stamps = {}

current_cycle = 1
current_x = 1

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

# get the cycle values
interesting_cycles = [i for i in range(20, 221, 40)]
signal_strengths = [(cycle * time_stamps[cycle]) for cycle in interesting_cycles]

print(sum(signal_strengths))
