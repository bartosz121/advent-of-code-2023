import pytest
from main import part1, part2


@pytest.fixture
def test_input_1():
    with open("test.txt") as f:
        yield [line.strip() for line in f.readlines()]


@pytest.fixture
def test_input_2():
    with open("test2.txt") as f:
        yield [line.strip() for line in f.readlines()]


def test_part1(test_input_1):
    assert part1(test_input_1) == 142


def test_part2(test_input_2):
    assert part2(test_input_2) == 281
