from collections import Counter

from get_data import get_data

data = get_data(2021, 14)
template, pairs = data.split("\n\n")
rules = {}
for i in pairs.splitlines():
    pair = i.split(" -> ")
    rules[pair[0]] = pair[1]


def apply_rules(template, rules, iterations=10):
    counts = {pair: Counter(pair) for pair in rules.keys()}
    for _ in range(iterations):
        new_counts = {}
        for pair, insert in rules.items():
            c = counts[pair[0] + insert] + counts[insert + pair[1]]
            c[insert] -= 1
            new_counts[pair] = c
        counts = new_counts

    c = Counter()
    for i in range(len(template) - 1):
        c += counts[template[i : i + 2]]
    c -= Counter(template[1:-1])
    return c.most_common()[0][1] - c.most_common()[-1][1]


print(apply_rules(template, rules))
print(apply_rules(template, rules, iterations=40))
