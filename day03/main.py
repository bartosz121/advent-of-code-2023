from functools import reduce
from operator import mul
from string import punctuation

SPECIAL_CHARACTERS = set(punctuation)
SPECIAL_CHARACTERS.remove(".")

SIDES = (
    (-1, 0),
    (-1, 1),
    (0, 1),
    (1, 1),
    (1, 0),
    (1, -1),
    (0, -1),
    (-1, -1),
)


def part1(input: list[str]) -> int:
    result = 0
    found_numbers: set[tuple[int, int]] = set()

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char in SPECIAL_CHARACTERS:
                current = (y, x)
                for side in SIDES:
                    candidate = (
                        current[0] - side[0],
                        current[1] - side[1],
                    )
                    if (n := input[candidate[0]][candidate[1]]).isdigit():
                        xl = candidate[1] - 1
                        # left
                        while xl >= 0:
                            if (xl_n := input[candidate[0]][xl]).isdigit():
                                n = xl_n + n
                                xl -= 1
                            else:
                                break
                        # right
                        xr = candidate[1] + 1
                        while xr < len(input[0]):
                            if (xr_n := input[candidate[0]][xr]).isdigit():
                                n = n + xr_n
                                xr += 1
                            else:
                                break

                        found_number_start_pos = (candidate[0], xl)
                        if not found_number_start_pos in found_numbers:
                            found_numbers.add(found_number_start_pos)
                            result += int(n)

    return result




def part2(input: list[str]) -> int:
    result = 0
    found_numbers_total: set[tuple[int, int]] = set()

    for y, line in enumerate(input):
        for x, char in enumerate(line):
            if char == "*":
                char_result = 1
                found_numbers: set[tuple[int, int]] = set()
                current = (y, x)

                for side in SIDES:
                    candidate = (
                        current[0] - side[0],
                        current[1] - side[1],
                    )
                    if (n := input[candidate[0]][candidate[1]]).isdigit():
                        xl = candidate[1] - 1
                        # left
                        while xl >= 0:
                            if (xl_n := input[candidate[0]][xl]).isdigit():
                                n = xl_n + n
                                xl -= 1
                            else:
                                break
                        # right
                        xr = candidate[1] + 1
                        while xr < len(input[0]):
                            if (xr_n := input[candidate[0]][xr]).isdigit():
                                n = n + xr_n
                                xr += 1
                            else:
                                break

                        found_number_start_pos = (candidate[0], xl)
                        if not found_number_start_pos in found_numbers and not found_number_start_pos in found_numbers_total:
                            if len(found_numbers) > 2:
                                break
                            found_numbers.add(found_number_start_pos)
                            char_result *= int(n)

                if len(found_numbers) == 2:
                    result += char_result
                    found_numbers_total.update(found_numbers)


    return result


if __name__ == "__main__":
    with open("input.txt") as f:
        input = [line.strip() for line in f.readlines()]
    print(f"{part1(input)=}")
    print(f"{part2(input)=}")
