from get_data import get_data

data = get_data(2025, 5).split("\n\n")

ranges = [tuple(map(int, i.split("-"))) for i in data[0].split()]
ids = list(map(int, data[1].split()))

ranges.sort()

part1 = 0
for i in ids:
    for start, end in ranges:
        if start <= i <= end:
            part1 += 1
            break
print(part1)

merged_ranges = []
curr_start, curr_end = ranges[0]
for next_start, next_end in ranges[1:]:
    if next_start <= curr_end + 1:
        curr_end = max(curr_end, next_end)
    else:
        merged_ranges.append((curr_start, curr_end))
        curr_start, curr_end = next_start, next_end
merged_ranges.append((curr_start, curr_end))

part2 = sum(end - start + 1 for start, end in merged_ranges)
print(part2)
