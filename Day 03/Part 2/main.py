# Advent of Code 2023 - Day 3 - Part 2
# https://adventofcode.com/2023/day/3#part2

def get_number(line, index):
    number = ""

    while (index < len(line) and line[index].isnumeric()):
        number += line[index]
        index += 1

    return int(number)

def is_part_number(lines, len_nbr, x, y):
    for i in range(x - 1, x + len_nbr + 1):
        if (i >= 0 and i < len(lines[y])):
            if (y != 0 and lines[y - 1][i] == "*"):
                return (str(y - 1) + ":" + str(i))
            if (y != len(lines) - 1 and lines[y + 1][i] == "*"):
                return (str(y + 1) + ":" + str(i))
            if (lines[y][i] == "*"):
                return (str(y) + ":" + str(i))

    return None

def get_index(lst, element):
    return [i for i, x in enumerate(lst) if x == element]

def remove_duplicates(lst):
    return [list(item) for item in set(tuple(sublist) for sublist in lst)]

def gear_ratios(part_numbers, gears_co):
    all_ratios = []
    all_cos = []

    for i in range(len(part_numbers)):
        index = get_index(gears_co, gears_co[i])
        if (len(index) > 1):
            all_cos.append(index)

    all_cos = remove_duplicates(all_cos)

    for i in range(len(all_cos)):
        ratio = part_numbers[all_cos[i][0]] * part_numbers[all_cos[i][1]]
        all_ratios.append(ratio)

    print(sum(all_ratios))

def main():
    part_numbers = []
    gears_co = []

    with open("Day 03/puzzle_input.txt", "r") as file:
        lines = [line.strip() for line in file.readlines()]

    for y, line in enumerate(lines):
        x = 0

        while (x < len(line)):
            if (line[x].isnumeric()):
                number = get_number(line, x)
                len_nbr = len(str(number))
                co = is_part_number(lines, len_nbr, x, y)
                if (co != None):
                    gears_co.append(co)
                    part_numbers.append(number)
                x += len_nbr
            else:
                x += 1

    gear_ratios(part_numbers, gears_co)

if __name__ == "__main__":
    main()
