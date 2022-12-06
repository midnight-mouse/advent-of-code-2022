with open("input.txt") as f:
    datastream = f.read().strip()

for i in range(0, len(datastream) - 3):
    if len(set(list(datastream[i:i+4]))) == 4:
        break

print(f'First marker after {i+4}')
