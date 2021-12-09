from adventofcode2021.dive import dive_part_1, dive_part_2

# Arrange
test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


def test_dive_part_1():
    # Act
    result = dive_part_1(test_input)

    # Assert
    assert result == 150


def test_dive_part_2():
    # Act
    result = dive_part_2(test_input)

    # Assert
    assert result == 900
