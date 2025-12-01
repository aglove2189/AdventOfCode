import os
import urllib.request
import argparse

AOC_SESSION = os.environ["AOC_SESSION"]


def get_data(year, day):
    """
    Get data for day (1-25) and year (>= 2015)
    User's session cookie is needed (puzzle inputs differ by user)
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    fn = f"{year}/day{day:02}.txt"
    fp = os.path.abspath(os.path.join(os.path.dirname(__file__), "../data", fn))
    if os.path.exists(fp):
        data = open(fp, "r").read()
    else:
        req = urllib.request.Request(url)
        req.add_header("Cookie", f"session={AOC_SESSION}")

        with urllib.request.urlopen(req) as response:
            data = response.read().decode("utf8")

        os.makedirs(os.path.dirname(fp), exist_ok=True)
        open(fp, "w").write(data)

    return data.rstrip("\r\n")


def main():
    parser = argparse.ArgumentParser(description="Get data for Advent of Code.")
    parser.add_argument("year", type=int, help="The year of the puzzle.")
    parser.add_argument("day", type=int, help="The day of the puzzle.")
    args = parser.parse_args()

    get_data(args.year, args.day)


if __name__ == "__main__":
    main()
