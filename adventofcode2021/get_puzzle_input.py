import requests

cookie = open("cookie.txt", "r").readline()


def get_puzzle_input(year: int, day: int) -> str:
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": cookie}

    return requests.get(url, cookies=cookies).text
