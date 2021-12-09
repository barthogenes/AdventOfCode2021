from binary_diagnostic import (
    binary_diagnostic_part_1,
    binary_diagnostic_part_2,
)
from dive import dive_part_1, dive_part_2
from get_puzzle_input import get_puzzle_input
from sonar_sweep import sonar_sweep_part_1, sonar_sweep_part_2

if __name__ == "__main__":
    puzzle_input = get_puzzle_input(2021, 1)
    print("Day 1: Sonar Sweep")
    print(f"Part 1 answer = {sonar_sweep_part_1(puzzle_input)}")
    print(f"Part 2 answer = {sonar_sweep_part_2(puzzle_input)}")

    puzzle_input = get_puzzle_input(2021, 2)
    print("Day 2: Dive!")
    print(f"Part 1 answer = {dive_part_1(puzzle_input)}")
    print(f"Part 2 answer = {dive_part_2(puzzle_input)}")

    puzzle_input = get_puzzle_input(2021, 3)
    print("Day 3: Binary Diagnostic")
    print(f"Part 1 answer = {binary_diagnostic_part_1(puzzle_input)}")
    print(f"Part 2 answer = {binary_diagnostic_part_2(puzzle_input)}")
