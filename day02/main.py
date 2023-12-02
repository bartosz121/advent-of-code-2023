import re
from functools import reduce
from operator import mul


def part1(input: list[str]) -> int:
    result = 0

    for game in input:
        d = {
            color: max(
                (
                    int(match[0])
                    for match in re.findall(r"(\d+) (red|green|blue)", game)
                    if match[1] == color
                )
            )
            for color in ("red", "green", "blue")
        }
        if d["red"] <= 12 and d["green"] <= 13 and d["blue"] <= 14:
            result += int(re.findall(r"Game (\d+)", game)[0])

    return result


def part2(input: list[str]) -> int:
    result = 0

    for game in input:
        d = {
            color: max(
                (
                    int(match[0])
                    for match in re.findall(r"(\d+) (red|green|blue)", game)
                    if match[1] == color
                )
            )
            for color in ("red", "green", "blue")
        }

        result += reduce(mul, d.values())

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [line.strip() for line in f.readlines()]
    print(f"{part1(input)=}")
    print(f"{part2(input)=}")
