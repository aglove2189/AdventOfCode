import argparse
import os
import re
import sys
import time
import urllib.parse
import urllib.request

AOC_SESSION = os.environ["AOC_SESSION"]


def countdown(message: str):
    minutes_match = re.search(r"(\d+)m", message)
    seconds_match = re.search(r"(\d+)s", message)

    minutes = int(minutes_match.group(1)) if minutes_match else 0
    seconds = int(seconds_match.group(1)) if seconds_match else 0

    total_seconds = (minutes * 60) + seconds

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"Waiting for: {mins:02d}m {secs:02d}s   ", end="\r")
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1


def submit(year, day, part, answer):
    """
    Submit an answer for a given day and part.
    """
    url = f"https://adventofcode.com/{year}/day/{day}/answer"
    data = urllib.parse.urlencode({"level": part, "answer": answer}).encode("utf-8")

    req = urllib.request.Request(url)
    req.add_header("Cookie", f"session={AOC_SESSION}")

    with urllib.request.urlopen(req, data=data) as response:
        response_text = response.read().decode("utf-8")
        match = re.search(r"<article>(.*?)<a href", response_text)
        message = re.sub(r"<[^>]+>", "", match.group(1)).strip()
        print(message)

        if "left to wait" in message:
            countdown(message)


def main():
    parser = argparse.ArgumentParser(description="Submit an answer for Advent of Code.")
    parser.add_argument("year", type=int, help="The year of the puzzle.")
    parser.add_argument("day", type=int, help="The day of the puzzle.")
    parser.add_argument("part", type=int, choices=[1, 2], help="The part of the puzzle (1 or 2).")
    parser.add_argument("answer", help="Your answer to the puzzle.")
    args = parser.parse_args()

    submit(args.year, args.day, args.part, args.answer)


if __name__ == "__main__":
    main()
