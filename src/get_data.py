import os
import urllib.request

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
