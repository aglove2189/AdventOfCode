from get_data import get_data

data = get_data(2025, 2).split(",")

part1 = 0
part2 = 0
for i in data:
    start, end = map(int, i.split("-"))
    for j in range(start, end + 1):
        s = str(j)
        l = len(s)
        mid = l // 2

        if s[:mid] == s[mid:]:
            part1 += j

        for k in range(1, mid + 1):
            if s[:k] * (l // k) == s:
                part2 += j
                break

print(part1)
print(part2)
