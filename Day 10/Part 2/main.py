# Advent of Code 2023 - Day 10 - Part 2
# https://adventofcode.com/2023/day/10#part2

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

def empty_map(lines):
    only_path = []

    for i in range(0, len(lines)):
        only_path.append("." * len(lines[0]))

    return only_path

def change_start(only_path, fstep, lstep):
    start = find_start(only_path)
    all_directions = ["NS", "EW", "NE", "NW", "SW", "SE"]
    all_pipes = ["|", "-", "L", "J", "7", "F"]
    directions = ""

    if (fstep[0] - start[0] == -1):
        directions += 'N'
    elif (fstep[0] - start[0] == 1):
        directions += 'S'
    elif (fstep[1] - start[1] == -1):
        directions += 'W'
    elif (fstep[1] - start[1] == 1):
        directions += 'E'

    if (lstep[0] - start[0] == -1):
        directions += 'N'
    elif (lstep[0] - start[0] == 1):
        directions += 'S'
    elif (lstep[1] - start[1] == -1):
        directions += 'W'
    elif (lstep[1] - start[1] == 1):
        directions += 'E'

    only_path[start[0]] = change_char(only_path[start[0]], start[1], all_pipes[all_directions.index(directions)])

    return only_path

def find_path(lines):
    only_path = empty_map(lines)
    start = find_start(lines)
    pos = start
    char = lines[pos[0]][pos[1]]
    only_path[pos[0]] = change_char(only_path[pos[0]], pos[1], char)
    lines[pos[0]] = change_char(lines[pos[0]], pos[1], '@')
    first_step = None
    last_step = None
    i = 0

    while True:
        last_step = pos
        pos = find_next(lines, pos[0], pos[1], char)
        char = lines[pos[0]][pos[1]]
        only_path[pos[0]] = change_char(only_path[pos[0]], pos[1], char)
        lines[pos[0]] = change_char(lines[pos[0]], pos[1], '@')
        i += 1
        if (char == 'S'):
            break
        if (i == 1):
            first_step = pos
        if (i == 2):
            lines[start[0]] = change_char(lines[start[0]], start[1], 'S')

    only_path = change_start(only_path, first_step, last_step)

    return only_path

def change_state(var):
    if (var == True):
        return False
    else:
        return True

def enclosed_tiles(lines):
    enclosed = 0

    for line in lines:
        into = False
        last_bend = ''

        for char in line:
            if (char == '.' and into == True):
                enclosed += 1

            if (char == '|'):
                into = change_state(into)

            if (char == 'L'):
                if (last_bend != ''):
                    if (last_bend == '7'):
                        into = change_state(into)
                    last_bend = ''
                else:
                    last_bend = 'L'

            if (char == 'J'):
                if (last_bend != ''):
                    if (last_bend == 'F'):
                        into = change_state(into)
                    last_bend = ''
                else:
                    last_bend = 'J'

            if (char == '7'):
                if (last_bend != ''):
                    if (last_bend == 'L'):
                        into = change_state(into)
                    last_bend = ''
                else:
                    last_bend = '7'

            if (char == 'F'):
                if (last_bend != ''):
                    if (last_bend == 'J'):
                        into = change_state(into)
                    last_bend = ''
                else:
                    last_bend = 'F'

    return enclosed

def main():
    with open("Day 10/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = find_path(lines)

    print(enclosed_tiles(lines))

if __name__ == "__main__":
    main()
