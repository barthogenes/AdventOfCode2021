from adventofcode2021.sonar_sweep import sonar_sweep


def test_sonar_sweep():
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

    # Act
    result = sonar_sweep(test_input)

    # Assert
    assert result == 7
