from get_data import get_data

data = list(map(int, get_data(2021, 6).split(",")))


def simulate(data, days=80):
    fish = [data.count(i) for i in range(9)]
    for _ in range(days):
        new_fish = fish.pop(0)
        fish[6] += new_fish
        fish.append(new_fish)
    return sum(fish)


print(simulate(data))
print(simulate(data, 256))
