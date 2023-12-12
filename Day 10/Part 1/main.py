# Advent of Code 2023 - Day 10 - Part 1
# https://adventofcode.com/2023/day/10#part1

def find_start(lines):
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "S":
                return y, x

def s_next(lines, y, x):
    if (lines[y - 1][x] == '|' or lines[y - 1][x] == '7' or lines[y - 1][x] == 'F'):
        return y - 1, x
    if (lines[y + 1][x] == '|' or lines[y + 1][x] == 'L' or lines[y + 1][x] == 'J'):
        return y + 1, x
    if (lines[y][x + 1] == '-' or lines[y][x + 1] == 'J' or lines[y][x + 1] == '7'):
        return y, x + 1
    if (lines[y][x - 1] == '-' or lines[y][x - 1] == 'L' or lines[y][x - 1] == 'F'):
        return y, x - 1

def v_pipe(lines, y, x):
    if (lines[y - 1][x] == '|' or lines[y - 1][x] == '7' or lines[y - 1][x] == 'F' or lines[y - 1][x] == 'S'):
        return y - 1, x
    if (lines[y + 1][x] == '|' or lines[y + 1][x] == 'L' or lines[y + 1][x] == 'J' or lines[y + 1][x] == 'S'):
        return y + 1, x

def h_pipe(lines, y, x):
    if (lines[y][x + 1] == '-' or lines[y][x + 1] == 'J' or lines[y][x + 1] == '7' or lines[y][x + 1] == 'S'):
        return y, x + 1
    if (lines[y][x - 1] == '-' or lines[y][x - 1] == 'L' or lines[y][x - 1] == 'F' or lines[y][x - 1] == 'S'):
        return y, x - 1

def l_pipe(lines, y, x):
    if (lines[y - 1][x] == '|' or lines[y - 1][x] == '7' or lines[y - 1][x] == 'F' or lines[y - 1][x] == 'S'):
        return y - 1, x
    if (lines[y][x + 1] == '-' or lines[y][x + 1] == 'J' or lines[y][x + 1] == '7' or lines[y][x + 1] == 'S'):
        return y, x + 1

def j_pipe(lines, y, x):
    if (lines[y - 1][x] == '|' or lines[y - 1][x] == '7' or lines[y - 1][x] == 'F' or lines[y - 1][x] == 'S'):
        return y - 1, x
    if (lines[y][x - 1] == '-' or lines[y][x - 1] == 'L' or lines[y][x - 1] == 'F' or lines[y][x - 1] == 'S'):
        return y, x - 1

def seven_pipe(lines, y, x):
    if (lines[y + 1][x] == '|' or lines[y + 1][x] == 'L' or lines[y + 1][x] == 'J' or lines[y + 1][x] == 'S'):
        return y + 1, x
    if (lines[y][x - 1] == '-' or lines[y][x - 1] == 'L' or lines[y][x - 1] == 'F' or lines[y][x - 1] == 'S'):
        return y, x - 1

def f_pipe(lines, y, x):
    if (lines[y + 1][x] == '|' or lines[y + 1][x] == 'L' or lines[y + 1][x] == 'J' or lines[y + 1][x] == 'S'):
        return y + 1, x
    if (lines[y][x + 1] == '-' or lines[y][x + 1] == 'J' or lines[y][x + 1] == '7' or lines[y][x + 1] == 'S'):
        return y, x + 1

def find_next(lines, y, x, char):
    if char == 'S':
        return s_next(lines, y, x)
    elif char == '|':
        return v_pipe(lines, y, x)
    elif char == '-':
        return h_pipe(lines, y, x)
    elif char == 'L':
        return l_pipe(lines, y, x)
    elif char == 'J':
        return j_pipe(lines, y, x)
    elif char == '7':
        return seven_pipe(lines, y, x)
    elif char == 'F':
        return f_pipe(lines, y, x)

def change_char(s, index, char):
    s_list = list(s)
    s_list[index] = char
    return ''.join(s_list)

def find_path(lines):
    start = find_start(lines)
    pos = start
    char = lines[pos[0]][pos[1]]
    lines[pos[0]] = change_char(lines[pos[0]], pos[1], '@')
    i = 0

    while True:
        pos = find_next(lines, pos[0], pos[1], char)
        char = lines[pos[0]][pos[1]]
        lines[pos[0]] = change_char(lines[pos[0]], pos[1], '@')
        i += 1
        if (char == 'S'):
            break
        if (i == 2):
            lines[start[0]] = change_char(lines[start[0]], start[1], 'S')

    return i

def main():
    with open("Day 10/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    print(int(find_path(lines) / 2))

if __name__ == "__main__":
    main()
