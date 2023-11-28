import os
import sys

template = """from get_data import get_data\n

data = get_data({year}, {day})\n"""


if __name__ == "__main__":
    year = sys.argv[1]
    fp = os.path.abspath(os.path.join(os.path.dirname(__file__), year))
    os.makedirs(fp, exist_ok=True)
    for day in range(1, 26):
        fn = f"{fp}/day{day:02}.py"
        if not os.path.exists(fn):
            with open(fn, "w") as f:
                f.write(template.format(year=year, day=day))
