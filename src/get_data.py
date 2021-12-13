# -*- coding: utf-8 -*-
import os
import urllib3
import requests
from config import session

urllib3.disable_warnings()


def get_data(year, day):
    """
    Get data for day (1-25) and year (>= 2015)
    User's session cookie is needed (puzzle inputs differ by user)
    """
    url = f"https://adventofcode.com/{year}/day/{day}/input"

    fn = f"{year}/day{day:02}.txt"
    fp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data', fn))
    if os.path.exists(fp):
        data = open(fp, "r").read()
    else:
        response = requests.get(url=url, cookies={"session": session}, verify=False)
        response.raise_for_status()

        os.makedirs(os.path.dirname(fp), exist_ok=True)
        data = response.text
        open(fp, "w").write(data)

    return data.rstrip("\r\n")
