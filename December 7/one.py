with open("input.txt") as f:
    lines = f.read().strip().split('\n')

directories = {'/': []}
pwd = '/'

def move(pwd, dest):

    # If pwd /home/dir return /home
    if dest == '..':
        new = pwd[:pwd.rindex('/')]
        return new if new != '' else '/'

    # if pwd /home and folder=dir, return /home/r
    return pwd + '/' + dest if pwd != '/' else pwd + dest

for line in lines[1:]:
    # change directory
    if line.startswith('$'):
        if 'cd' in line:
            pwd = move(pwd, line.replace('$ cd ', ''))
            
            # add entry for directory
            if pwd not in directories:
                directories[pwd] = []
    else:
        # append files and sizes 
        if 'dir' not in line:
            size, name = line.split(' ')
            # check if name is not already added
            if sum([name in item[1] for item in directories[pwd]]) == 0:
                directories[pwd].append((int(size), name))

# turn files into sizes
file_sum = lambda files: sum([f[0] for f in files])
own_sizes = {key: file_sum(files) for key, files in directories.items()}
tot_sizes = {key: 0 for key in own_sizes.keys()}

for parent_key in own_sizes.keys():
    # find all paths that starts with
    paths = [k for k in own_sizes if k.startswith(parent_key)]

    # add all these to tot sizes
    for p in paths:
        tot_sizes[parent_key] += own_sizes[p]

# get all directories size <= 100000
total_size = sum([d_size for d_size in tot_sizes.values() if d_size < 100000])
print(total_size)

"""
filetree = {
 '/': [
        'file.txt',
        'a': {
            ('test2.txt', 1100),
            ('test3.txt', 34234)
        },
        'b': {
            'c': {
                ('sfdsdf', 34234)
            }
        }
    ]   
}

alt

directories = {
    '/': 22323,
    '/home': 3424,
    '/a': 31232,
    '/a/b': 2343
}
"""