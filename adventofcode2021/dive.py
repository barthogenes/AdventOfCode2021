def dive_part_1(input: str):
    horizontal_position = 0
    depth = 0
    for line in input.splitlines():
        words = line.split(" ")
        if words[0] == "forward":
            horizontal_position += int(words[1])

        if words[0] == "down":
            depth += int(words[1])

        if words[0] == "up":
            depth -= int(words[1])

    return horizontal_position * depth


def dive_part_2(input: str):
    return 0
