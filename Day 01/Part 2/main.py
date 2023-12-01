# Advent of Code 2023 - Day 1 - Part 2
# https://adventofcode.com/2020/day/1#part2

def detect_number(line, index):
    numbers_letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number = ""

    for char in line[index:]:
        number += char

        if (number in numbers_letters):
            return str(numbers_letters.index(number) + 1)

    return None

def main():
    all_numbers = []

    with open("puzzle_input.txt", "r") as file:
        lines = file.readlines()

    for line in lines:
        each_number = []
        number = 0

        for index, char in enumerate(line.strip()):
            if (char.isnumeric()):
                each_number.append(char)
            else:
                dn = detect_number(line, index)

                if (dn != None):
                    each_number.append(dn)

        if (len(each_number) == 1):
            number = each_number[0] + each_number[0]
        else:
            number = each_number[0] + each_number[-1]

        print(each_number)
        all_numbers.append(int(number))

    print(sum(all_numbers))

if __name__ == "__main__":
    main()
