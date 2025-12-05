from get_data import get_data

data = get_data(2025, 5).split("\n\n")

ranges = [tuple(map(int, i.split("-"))) for i in data[0].split()]
ids = list(map(int, data[1].split()))

ranges.sort()

part1 = 0
for i in ids:
    is_fresh = False
    for start, end in ranges:
        if start <= i <= end:
            is_fresh = True
            break
        if start > i:
            break
    if is_fresh:
        part1 += 1

print(part1)

merged_ranges = []
curr_start, curr_end = ranges[0]
for i in range(1, len(ranges)):
    next_start, next_end = ranges[i]
    if next_start <= curr_end + 1:
        curr_end = max(curr_end, next_end)
    else:
        merged_ranges.append((curr_start, curr_end))
        curr_start, curr_end = next_start, next_end
merged_ranges.append((curr_start, curr_end))

part2 = sum(end - start for start, end in merged_ranges) + len(merged_ranges)
print(part2)
