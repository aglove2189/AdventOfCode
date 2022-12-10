from get_data import get_data

data = get_data("2022", "10").split()

x, part1, part2 = 1, 0, "\n"
for i, d in enumerate(data, 1):
    part1 += i * x if i % 40 == 20 else 0
    part2 += "#" if abs((i - 1) % 40 - x) < 2 else "\n" if i % 40 == 0 else " "
    x += int(d) if d[-1].isdigit() else 0

print(part1)
print(*part2)
