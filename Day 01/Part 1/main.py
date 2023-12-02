# Advent of Code 2023 - Day 1 - Part 1
# https://adventofcode.com/2023/day/1#part1

def main():
    all_numbers = []

    with open("Day 01/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        each_number = []
        number = 0

        for char in line.strip():
            if (char.isnumeric()):
                each_number.append(char)

        if (len(each_number) == 1):
            number = each_number[0] + each_number[0]
        else:
            number = each_number[0] + each_number[-1]

        all_numbers.append(int(number))

    print(sum(all_numbers))

if __name__ == "__main__":
    main()
