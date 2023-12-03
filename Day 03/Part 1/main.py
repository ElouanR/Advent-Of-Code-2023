# Advent of Code 2023 - Day 3 - Part 1
# https://adventofcode.com/2023/day/3#part1

def get_number(line, index):
    number = ""

    while (index < len(line) and line[index].isnumeric()):
        number += line[index]
        index += 1

    return int(number)

def is_part_number(lines, len_nbr, x, y, number):
    for i in range(x - 1, x + len_nbr + 1):
        if (i >= 0 and i < len(lines[y])):
            if (y != 0 and lines[y - 1][i] != "." and not lines[y - 1][i].isnumeric()):
                return True
            if (y != len(lines) - 1 and lines[y + 1][i] != "." and not lines[y + 1][i].isnumeric()):
                return True
            if (lines[y][i] != "." and not lines[y][i].isnumeric()):
                return True

    return False

def main():
    part_numbers = []

    with open("Day 03/puzzle_input.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for y, line in enumerate(lines):
        x = 0

        while (x < len(line)):
            if (line[x].isnumeric()):
                number = get_number(line, x)
                len_nbr = len(str(number))
                if (is_part_number(lines, len_nbr, x, y, number)):
                    part_numbers.append(number)
                x += len_nbr
            else:
                x += 1

    print(sum(part_numbers))

if __name__ == "__main__":
    main()
