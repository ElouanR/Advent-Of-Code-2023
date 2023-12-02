# Advent of Code 2023 - Day 2 - Part 1
# https://adventofcode.com/2023/day/2#part1

def main():
    ids_possible = []

    with open("Day 02/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    for id, line in enumerate(lines, start = 1):
        possible = True
        line = line.split(": ", 1)[1]
        list_sets = line.split("; ")

        for set in list_sets:
            set = set.strip().split(", ")

            for cube in set:
                cube = cube.split(" ")

                match cube[1]:
                    case "red":
                        if (int(cube[0]) > 12):
                            possible = False
                    case "green":
                        if (int(cube[0]) > 13):
                            possible = False
                    case "blue":
                        if (int(cube[0]) > 14):
                            possible = False

                if (not possible):
                    break

            if (not possible):
                break

        if (possible):
            ids_possible.append(id)

    print(sum(ids_possible))

if __name__ == "__main__":
    main()
