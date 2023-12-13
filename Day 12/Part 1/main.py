# Advent of Code 2023 - Day 12 - Part 1
# https://adventofcode.com/2023/day/12#part1

def generate_combinations(input_string, i):
    if (i < len(input_string)):
        if (input_string[i] == '?'):
            for char in ['.', '#']:
                yield from generate_combinations(input_string[:i] + char + input_string[i + 1:], i + 1)
        else:
            yield from generate_combinations(input_string, i + 1)
    else:
        yield input_string

def main():
    with open("Day 12/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip().split() for line in lines]
    sum_arrangements = 0

    for line in lines:
        tmp = line[1].split(',')
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        line[1] = tmp

        for combination in generate_combinations(line[0], 0):
            tmp = combination.split('.')
            tmp = [tmp for tmp in tmp if tmp != '']
            tmp = [len(tmp) for tmp in tmp]

            if (tmp == line[1]):
                sum_arrangements += 1

    print(sum_arrangements)

if __name__ == "__main__":
    main()
