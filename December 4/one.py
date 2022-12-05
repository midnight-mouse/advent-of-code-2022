with open('input.txt') as f:
    contents = f.read().strip().split('\n')

# produce ranges
ranges = [segment.split('-') for row in contents for segment in row.split(',')]
ranges = [set(range(int(segment[0]), int(segment[1]) + 1)) for segment in ranges]

# check how many sets is contained in one another
contains = sum([(a | b == a) or (a | b == b) for a, b in zip(ranges[::2], ranges[1::2])])

print(contains)