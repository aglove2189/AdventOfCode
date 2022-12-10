import re

from get_data import get_data


def valid_int(i, min_, max_):
    try:
        i = int(i)
        return min_ <= i <= max_
    except ValueError:
        return False


def valid_hgt(i):
    if "cm" in i:
        return 150 <= int(i.replace("cm", "")) <= 193
    elif "in" in i:
        return 59 <= int(i.replace("in", "")) <= 76
    return False


data = get_data(2020, 4).split("\n\n")

req_keys = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
part1 = 0
part2 = 0
for d in data:
    passport = d.split()
    p = dict(i.split(":") for i in passport)
    part1 += all(k in p for k in req_keys)
    try:
        part2 += all(
            (
                valid_int(p["byr"], 1920, 2002),
                valid_int(p["iyr"], 2010, 2020),
                valid_int(p["eyr"], 2020, 2030),
                valid_hgt(p["hgt"]),
                re.match(r"^#[0-9a-f]{6}$", p["hcl"]) is not None,
                re.match(r"^\d{9}$", p["pid"]) is not None,
                p["ecl"] in ("amb", "blu", "brn", "gry", "hzl", "oth"),
            )
        )
    except KeyError:
        pass
print(part1)
print(part2)
