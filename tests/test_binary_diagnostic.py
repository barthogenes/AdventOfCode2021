from adventofcode2021.binary_diagnostic import binary_diagnostic_part_1

# Arrange
test_input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def test_binary_diagnostic_part_1():
    # Act
    result = binary_diagnostic_part_1(test_input)

    # Assert
    assert result == 198
