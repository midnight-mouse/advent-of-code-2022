with open("input.txt") as f:
    datastream = f.read().strip()

for i in range(0, len(datastream) - 13):
    if len(set(list(datastream[i:i+14]))) == 14:
        break

print(f'First marker after {i+14}')