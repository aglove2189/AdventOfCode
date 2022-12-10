import re
from collections import defaultdict

from get_data import get_data

data = get_data(2020, 7).splitlines()


contained_in = defaultdict(set)
bags = defaultdict(list)
for d in data:
    bag, inner_bags = d.split(" bags contain ")
    inner_bags = re.sub(r" bags?\.?", "", inner_bags)
    inner_bags = inner_bags.split(", ")
    ib = []
    for i in inner_bags:
        contained_in[i[2::]].add(bag)
        try:
            bags[bag].append((int(i[0]), i[2::]))
        except ValueError:
            pass

part1 = set()


def check_if_contained(color):
    for c in contained_in[color]:
        part1.add(c)
        check_if_contained(c)


check_if_contained("shiny gold")
print(len(part1))


def check_num_bags(color):
    return sum(count + count * check_num_bags(bag) for count, bag in bags[color])


print(check_num_bags("shiny gold"))
