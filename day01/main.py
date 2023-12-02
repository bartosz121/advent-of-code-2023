import re


def part1(input: list[str]) -> int:
    return sum(
        map(
            lambda numbers: int(numbers[0] + numbers[-1]),
            [[char for char in line if char.isnumeric()] for line in input],
        )
    )


def part2(input: list[str]) -> int:
    result = 0
    replace_map = {
        "oneight": "18",
        "threeight": "38",
        "fiveight": "58",
        "nineight": "98",
        "twone": "21",
        "sevenine": "79",
        "eightwo": "82",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    pattern = "(" + "|".join(replace_map.keys()) + ")"
    for line in input:
        line2 = re.sub(pattern, lambda match: replace_map.get(match.group(0)), line)
        digits = [char for char in line2 if char.isdigit()]
        result += int(digits[0] + digits[-1])

    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [line.strip() for line in f.readlines()]
    # print(f"{part1(input)=}")
    print(f"{part2(input)=}")
