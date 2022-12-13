import ast

with open("input.txt") as f:
    contents = f.read().strip()

v = False

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

def bubble_sort(sequence):
    # perform bubble sort
    n = len(sequence)
    for i in range(n-1):
        for j in range(n-i-1):
            if (compare(sequence[j], sequence[j+1]) == False):
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]


# create list of all lists to compare
contents = contents.replace("\n\n", '\n').split('\n')
rows = [ast.literal_eval(s) for s in contents]

# insert divider elements
rows.append([[2]])
rows.append([[6]])

bubble_sort(rows)

if v:
    for r in rows:
        print(r)

# get index and their decoder key
decoder_key = (rows.index([[2]]) + 1) * (rows.index([[6]]) + 1)

print(f'Decoder key: {decoder_key}')