# Advent of Code 2023 - Day 4 - Part 1
# https://adventofcode.com/2023/day/4#part1

def main():
    sum = 0

    with open("Day 04/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip().split(": ")[-1] for line in lines]

    for i in range(len(lines)):
        worth = 0

        win_nbrs = lines[i].split(" | ")[0]
        win_nbrs = [nbr for nbr in win_nbrs.split(" ") if nbr != '']
        my_nbrs = lines[i].split(" | ")[1]
        my_nbrs = [nbr for nbr in my_nbrs.split(" ") if nbr != '']

        for j in range(len(my_nbrs)):
            if my_nbrs[j] in win_nbrs:
                if worth == 0:
                    worth = 1
                else:
                    worth *= 2

        sum += worth

    print(sum)

if __name__ == "__main__":
    main()
