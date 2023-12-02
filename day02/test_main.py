import pytest
from main import part1, part2


@pytest.fixture
def test_input():
    with open("test.txt") as f:
        yield [line.strip() for line in f.readlines()]


def test_part1(test_input):
    assert part1(test_input) == 8


def test_part2(test_input):
    assert part2(test_input) == 2286
