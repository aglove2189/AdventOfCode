from get_data import get_data


def run(data):
    return sum(int(n[0] + n[-1]) for n in [[i for i in d if i.isdigit()] for d in data])


data = get_data(2023, 1)
print(run(data.split()))

data = (
    data.replace("one", "o1e")
    .replace("two", "t2o")
    .replace("three", "t3e")
    .replace("four", "f4r")
    .replace("five", "f5e")
    .replace("six", "s6x")
    .replace("seven", "s7n")
    .replace("eight", "e8t")
    .replace("nine", "n9e")
)
print(run(data.split()))
