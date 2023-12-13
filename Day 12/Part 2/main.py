# Advent of Code 2023 - Day 12 - Part 2
# https://adventofcode.com/2023/day/12#part2

import time

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
    start_time = time.time()

    with open("Day 12/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip().split() for line in lines]
    sum_arrangements = 0

    for line in lines:
        line[0] = "?".join([line[0]] * 5)
        tmp = line[1].split(',')

        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])

        line[1] = tmp * 5

        for combination in generate_combinations(line[0], 0):
            tmp = combination.split('.')
            tmp = [tmp for tmp in tmp if tmp != '']
            tmp = [len(tmp) for tmp in tmp]

            if (tmp == line[1]):
                sum_arrangements += 1

    print(sum_arrangements)

    execution_time = time.time() - start_time
    print("Le temps d'exécution est {:.2f} secondes.".format(execution_time))

if __name__ == "__main__":
    main()
