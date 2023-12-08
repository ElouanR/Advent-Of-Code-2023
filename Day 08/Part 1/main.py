# Advent of Code 2023 - Day 8 - Part 1
# https://adventofcode.com/2023/day/8#part1

def steps(instructions, elements):
    current_element = "AAA"
    nbr_steps = 0

    while (1):
        for char in instructions:
            if char == "L":
                current_element = elements[current_element]["left"]
                nbr_steps += 1
            else:
                current_element = elements[current_element]["right"]
                nbr_steps += 1

            if current_element == "ZZZ":
                break

        if current_element == "ZZZ":
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

    print(steps(instructions, elements))

if __name__ == "__main__":
    main()
