# Advent of Code 2023 - Day 2 - Part 2
# https://adventofcode.com/2023/day/2#part2

def main():
    all_powers = []

    with open("Day 02/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        line = line.split(": ", 1)[1]
        list_sets = line.split("; ")
        min_red = 0
        min_green = 0
        min_blue = 0

        for set in list_sets:
            set = set.strip().split(", ")

            for cube in set:
                cube = cube.split(" ")

                match cube[1]:
                    case "red":
                        if (int(cube[0]) > min_red):
                            min_red = int(cube[0])
                    case "green":
                        if (int(cube[0]) > min_green):
                            min_green = int(cube[0])
                    case "blue":
                        if (int(cube[0]) > min_blue):
                            min_blue = int(cube[0])

        all_powers.append(min_red * min_green * min_blue)

    print(sum(all_powers))

if __name__ == "__main__":
    main()
