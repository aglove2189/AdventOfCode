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

    fn = "{year}/day{day}.txt".format(year=year, day=str(day).zfill(2))
    fp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data', fn))
    if os.path.exists(fp):
        data = open(fp, "r").read()
    else:
        response = requests.get(url=url, cookies={"session": session})
        response.raise_for_status()

        os.makedirs(os.path.dirname(fp), exist_ok=True)
        data = response.text
        open(fp, "w").write(data)

    return data.rstrip("\r\n")
