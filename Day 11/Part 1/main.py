# Advent of Code 2023 - Day 11 - Part 1
# https://adventofcode.com/2023/day/11#part1

def insert_char(s, index, char):
    return s[:index] + char + s[index:]

def change_char(s, index, char):
    s_list = list(s)
    s_list[index] = char
    return ''.join(s_list)

def expand(lines):
    i = 0
    x = 0

    while (i < len(lines)):
        if (len(set(lines[i])) == 1):
            lines.insert(i, lines[i])
            i += 1
        i += 1

    while (x < len(lines[0])):
        p = True

        for y in range(len(lines)):
            if (lines[y][x] != '.'):
                p = False
                break

        if (p):
            for y in range(len(lines)):
                lines[y] = insert_char(lines[y], x, '.')
            x += 1
        x += 1

    return lines

def get_coordinates(lines):
    coordinates = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (char == '#'):
                coordinates.append((y, x))

    return coordinates

def lenghts_paths(coordinates):
    all_lenghts = []
    i = 0

    while (i < len(coordinates)):
        j = i + 1

        while (j < len(coordinates)):
            all_lenghts.append(abs(coordinates[i][0] - coordinates[j][0]) + abs(coordinates[i][1] - coordinates[j][1]))
            j += 1
        i += 1

    return all_lenghts

def main():
    with open("Day 11/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = expand(lines)
    coordinates = get_coordinates(lines)
    all_lenghts = lenghts_paths(coordinates)

    print(sum(all_lenghts))

if __name__ == "__main__":
    main()
