# -*- coding: utf-8 -*-
import os
import requests
from config import session


def get_data(year, day):
    """
    Get data for day (1-25) and year (>= 2015)
    User's session cookie is needed (puzzle inputs differ by user)
    """

    url = "https://adventofcode.com/{year}/day/{day}/input".format(year=year, day=day)

    fp = "../data/{year}/day{day}.txt".format(year=year, day=str(day).zfill(2))
    if os.path.exists(fp):
        with open(fp, "r") as f:
            data = f.read()
    else:
        dirname = os.path.dirname(fp)
        os.makedirs(dirname, exist_ok=True)

        response = requests.get(url=url, cookies={"session": session})
        response.raise_for_status()
        data = response.text

        with open(fp, "w") as f:
            f.write(data)

    return data.rstrip("\r\n")
