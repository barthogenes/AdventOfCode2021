from adventofcode2021.sonar_sweep import sonar_sweep_part_1, sonar_sweep_part_2

# Arrange
test_input = """199
200
208
210
200
207
240
269
260
263"""


def test_sonar_sweep_part_1():
    # Act
    result = sonar_sweep_part_1(test_input)

    # Assert
    assert result == 7


def test_sonar_sweep_part_2():
    # Act
    result = sonar_sweep_part_2(test_input)

    # Assert
    assert result == 5
