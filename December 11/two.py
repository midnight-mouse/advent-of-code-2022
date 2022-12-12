import numpy as np

"""
Parse input:
monkeys = {
    0: {
        'items': [79, 98],
        'operation': ['*', 19],
        'test': 23,
        'true': 2,
        'false': 3
    }
}
"""

with open("input-small.txt") as f:
    contents = f.read()

monkeys = {}

descriptions = contents.split("\n\n")
for i, m_desc in enumerate(descriptions):

    monkeys[i] = {}
    stats = ["items", "operation", "test", "true", "false"]

    for stat, value in zip(stats, m_desc.split("\n")[1:]):
        if stat == "items":
            add = value.strip().replace("Starting items: ", "").split(", ")
            add = np.array([int(a) for a in add])
        if stat == "operation":
            add = value.strip().replace("Operation: new = old ", "").split(" ")
        if stat == "test":
            add = int(value.strip().replace("Test: divisible by ", ""))
        if stat == "true":
            add = int(value.strip().replace("If true: throw to monkey ", ""))
        if stat == "false":
            add = int(value.strip().replace("If false: throw to monkey ", ""))

        monkeys[i][stat] = add

    monkeys[i]["inspects"] = 0

# Play the game!
for i in range(10000):
    print(f"Round {i+1}...")

    for m in monkeys:
        monk = monkeys[m]

        for item in monk["items"]:
            # inspect item
            old = monk["items"][0]
            monk["items"] = monk["items"][1:]
            monk["inspects"] += 1

            # determine new worry level
            if "+" in monk["operation"]:
                new = old + int(monk["operation"][1])
            if "*" in monk["operation"]:
                if "old" in monk["operation"]:
                    new = old * old
                else:
                    new = old * int(monk["operation"][1])

            # check if divisible
            if new % monk["test"] == 0:
                # divide by this number
                new = new // monk["test"]
                monkeys[monk["true"]]["items"].append(new)

            else:
                monkeys[monk["false"]]["items"].append(new)

    # end of 1000's round
    if (i + 1) % 1000 == 0:
        print(f"== After round {i + 1} ==")
        for m in monkeys:
            print(f'Monkey {m} inspected items {monkeys[m]["inspects"]} times.')

        print()


# get two most active monkeys and multiply them
inspects = sorted([m["inspects"] for m in monkeys.values()])
monkeys_business = inspects[-1] * inspects[-2]

print(f"Monkey Business: {monkeys_business}")
