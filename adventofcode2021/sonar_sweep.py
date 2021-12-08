def sonar_sweep(input: str):
    val = float("inf")
    increased_count = 0
    for line in input.splitlines():
        num = int(line)
        if val < num:
            increased_count += 1

        val = num

    return increased_count
