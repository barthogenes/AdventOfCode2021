import requests

cookie = open("cookie.txt", "r").readline()


def get_puzzle_input(year: int, day: int) -> str:
    url = "https://adventofcode.com/2021/day/1/input"
    cookies = {"session": cookie}

    return requests.get(url, cookies=cookies).text
