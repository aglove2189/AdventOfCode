from get_data import get_data

data = get_data(2025, 1).split()

pos = 50
part1 = 0
part2 = 0
for i in data:
    direction = i[0]
    val = int(i[1:])
    if direction == "R":
        for j in range(0, val):
            pos += 1
            pos %= 100
            if pos == 0:
                part2 += 1
    else:
        for j in range(0, val):
            pos -= 1
            pos %= 100
            if pos == 0:
                part2 += 1

    if pos == 0:
        part1 += 1
print(part1)
print(part2)
