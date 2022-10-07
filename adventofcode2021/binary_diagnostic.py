import numpy as np


def get_transposed_input(input: str) -> np.ndarray:
    number_lines = []
    for line in input.splitlines():
        number_lines.append(np.fromiter(line, dtype=int))

    return np.stack(number_lines).transpose()


def binary_diagnostic_part_1(input: str):
    numbers = get_transposed_input(input)
    length = numbers.shape[1] / 2

    def to_most_common_bit(val: int):
        if val > length:
            return 1

        return 0

    vto_most_common_bit = np.vectorize(to_most_common_bit)

    binary_string = vto_most_common_bit(numbers.sum(axis=1))
    gamma_binary_string = ""
    epsilon_binary_string = ""
    for bit in binary_string:
        gamma_binary_string += str(bit)
        epsilon_binary_string += str(bit ^ 1)

    gamma = int(gamma_binary_string, 2)
    epsilon = int(epsilon_binary_string, 2)
    return gamma * epsilon


def binary_diagnostic_part_2(input: str):
    return 0
