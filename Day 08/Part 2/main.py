# Advent of Code 2023 - Day 8 - Part 2
# https://adventofcode.com/2023/day/8#part2

import math
from functools import reduce

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

def lcm_list(numbers):
    return reduce(lcm, numbers)

def get_start(elements):
    all_starts = []

    for element in elements:
        if element[2] == 'A':
            all_starts.append(element)

    return all_starts

def steps(instructions, elements, start_element):
    current_element = start_element
    nbr_steps = 0

    while (1):
        for char in instructions:
            if char == "L":
                current_element = elements[current_element]["left"]
                nbr_steps += 1
            else:
                current_element = elements[current_element]["right"]
                nbr_steps += 1

            if current_element[2] == 'Z':
                break

        if current_element[2] == 'Z':
                break

    return nbr_steps

def main():
    with open("Day 08/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    instructions = lines[0]
    elements = {}

    for line in lines[2:]:
        element = {}
        line = line.replace(" = (", " ").replace(", ", " ").replace(")", "").split(" ")
        element["left"] = line[1]
        element["right"] = line[2]
        elements[line[0]] = element

    all_starts = get_start(elements)
    all_steps = []

    for start in all_starts:
        all_steps.append(steps(instructions, elements, start))

    print(lcm_list(all_steps))

if __name__ == "__main__":
    main()
