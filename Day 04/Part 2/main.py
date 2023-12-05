# Advent of Code 2023 - Day 4 - Part 2
# https://adventofcode.com/2023/day/4#part2

def main():
    nbr_scratchcards = []

    with open("Day 04/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip().split(": ")[-1] for line in lines]

    for i in range(len(lines)):
        nbr_scratchcards.append(1)

    for i in range(len(lines)):
        worth = 0

        win_nbrs = lines[i].split(" | ")[0]
        win_nbrs = [nbr for nbr in win_nbrs.split(" ") if nbr != '']
        my_nbrs = lines[i].split(" | ")[1]
        my_nbrs = [nbr for nbr in my_nbrs.split(" ") if nbr != '']

        for j in range(len(my_nbrs)):
            if my_nbrs[j] in win_nbrs:
                worth += 1

        for x in range(1, worth + 1):
            nbr_scratchcards[i + x] += nbr_scratchcards[i]

    print(sum(nbr_scratchcards))

if __name__ == "__main__":
    main()
