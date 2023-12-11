# Advent of Code 2023 - Day 11 - Part 2
# https://adventofcode.com/2023/day/11#part2

expand_y = []
expand_x = []

def insert_char(s, index, char):
    return s[:index] + char + s[index:]

def change_char(s, index, char):
    s_list = list(s)
    s_list[index] = char
    return ''.join(s_list)

def expand(lines):
    global expand_y
    global expand_x
    i = 0
    x = 0

    while (i < len(lines)):
        if (len(set(lines[i])) == 1):
            expand_y.append(i)
        i += 1

    while (x < len(lines[0])):
        p = True

        for y in range(len(lines)):
            if (lines[y][x] != '.' and lines[y][x] != '@'):
                p = False
                break

        if (p):
            expand_x.append(x)
        x += 1

    return lines

def get_coordinates(lines):
    coordinates = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if (char == '#'):
                coordinates.append((y, x))

    return coordinates

def count_at_symbols(start, end):
    count = 0

    for y in expand_y:
        if (y > min(start[0], end[0]) and y < max(start[0], end[0])):
            count += 1

    for x in expand_x:
        if (x > min(start[1], end[1]) and x < max(start[1], end[1])):
            count += 1

    return count

def lenghts_paths(coordinates, lines):
    all_lenghts = []
    i = 0

    while (i < len(coordinates)):
        j = i + 1

        while (j < len(coordinates)):
            at_count = count_at_symbols(coordinates[i], coordinates[j])
            all_lenghts.append(abs(coordinates[i][0] - coordinates[j][0]) + abs(coordinates[i][1] - coordinates[j][1]) + (at_count * 1000000 - at_count))
            j += 1
        i += 1

    return all_lenghts

def main():
    with open("Day 11/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = expand(lines)
    coordinates = get_coordinates(lines)
    all_lenghts = lenghts_paths(coordinates, lines)

    print(sum(all_lenghts))

if __name__ == "__main__":
    main()
