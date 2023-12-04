from get_data import get_data

data = get_data(2023, 4).splitlines()

p1 = 0
copies = {i: 1 for i in range(len(data))}
for i, d in enumerate(data):
    _, d = d.split(":")
    winning, numbers = d.split("|")
    winning = winning.split()
    numbers = numbers.split()
    power = len([i for i in numbers if i in winning])
    if power > 0:
        p1 += 2 ** (power - 1)
    for j in range(power):
        copies[i + j + 1] += copies[i]

print(p1)
print(sum(copies.values()))
