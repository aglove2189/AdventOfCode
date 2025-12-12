from collections import defaultdict
from get_data import get_data

data = get_data(2022, 7).splitlines()

path = []
sizes = defaultdict(int)

for d in data:
    cmd = d.split()

    if cmd[0] == "$":
        if cmd[1] == "cd":
            if cmd[2] == "..":
                path.pop()
            elif cmd[2] == "/":
                path = []
            else:
                path.append(cmd[2])
    elif cmd[0] != "dir":
        size = int(cmd[0])
        sizes["/"] += size
        curr_path = ""
        for p in path:
            curr_path += "/" + p
            sizes[curr_path] += size

print(sum(s for s in sizes.values() if s <= 100000))

threshold = 30000000 - (70000000 - sizes["/"])
print(min(s for s in sizes.values() if s >= threshold))
