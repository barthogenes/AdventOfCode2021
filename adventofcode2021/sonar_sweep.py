def sonar_sweep_part_1(input: str):
    val = float("inf")
    increased_count = 0
    for line in input.splitlines():
        num = int(line)
        if val < num:
            increased_count += 1

        val = num

    return increased_count


def sonar_sweep_part_2(input: str):
    val = float("inf")
    increased_count = 0
    lines = input.splitlines()
    for i in range(len(lines) - 2):
        num = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        if val < num:
            increased_count += 1

        val = num

    return increased_count
