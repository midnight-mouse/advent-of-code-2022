import ast

with open("input.txt") as f:
    contents = f.read().strip().split("\n\n")


# create list of pairs
pairs = []
v = True

for pair in contents:
    pairs.append([ast.literal_eval(s) for s in pair.split("\n")])

def printv(message, verbose=False):
    if verbose:
        print(message)

def compare(a, b):

    printv(f'Compare {a} vs {b}', v)

    # int base cases
    if type(a) == int and type(b) == int:
        if a == b: return None
        if a < b: printv('Left side is smaller.', v); return True
        if a > b: printv('Right side is smaller.', v); return False
    
    # Mixed types
    if type(a) == int and type(b) == list:
        printv(f'Mixed types; convert left to [{a}]', v)
        a = [a]

    if type(a) == list and type(b) == int:
        printv(f'Mixed types; convert right to [{b}]', v)
        b = [b]

    # list base cases
    if len(a) == 0 and len(b) == 0: return None
    if len(a) == 0: printv('Left side ran out of items.', v); return True
    if len(b) == 0: printv('Right side ran out of items.', v); return False
    
    # recursively compare
    for i in range(len(a)):
        # right pair ran out of items first
        if i > len(b) - 1: printv('Right side ran out of items.', v); return False

        result = compare(a[i], b[i])

        if result == None: 
            continue
        
        return result

    # ran out of items
    if len(a) == len(b): return None

    printv('Left side ran out of items.', v)

    return True

# go through rules
indexes = []
for i, pair in enumerate(pairs):

    printv(f"== Pair {i + 1}: ==", v)

    input1, input2 = pair
    result = compare(input1, input2)

    if result == True: 
        printv('== Inputs are in the right order', v)
        indexes.append(i + 1)
    else:
        printv('== Inputs are NOT in the right order', v)

    printv('', v)

print(sum(indexes))
print(indexes)

# 41 is wrong! Why?