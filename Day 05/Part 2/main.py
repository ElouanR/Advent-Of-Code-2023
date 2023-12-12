# Advent of Code 2023 - Day 5 - Part 2
# https://adventofcode.com/2023/day/5#part2

from pprint import pprint

def get_min_location(almanac, seeds_pairs):
    pass

def init_almanac():
    almanac_names = ["seeds", "soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    almanac = {
        "seeds": [],
        "soil": [],
        "fertilizer": [],
        "water": [],
        "light": [],
        "temperature": [],
        "humidity": [],
        "location": []
    }
    almanac_nbr = 0
    i = 1

    with open("Day 05/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip().split() for line in lines]

    for j in range(len(lines[0][1:]) - 1):
        almanac[almanac_names[almanac_nbr]].append([lines[0][1:][j], lines[0][1:][j + 1]])

    while (i < len(lines)):
        if (lines[i] == []):
            almanac_nbr += 1
            i += 2
            continue
        almanac[almanac_names[almanac_nbr]].append(lines[i])
        i += 1

    return almanac

def get_location(almanac, seeds_range):
    almanac_names = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    sources_range = seeds_range

    for x in range(len(almanac_names)):
        temp = []
        for rangeee in sources_range:
            for i in range(len(almanac[almanac_names[x]])):
                nbr_destination = int(almanac[almanac_names[x]][i][0])
                nbr_source = int(almanac[almanac_names[x]][i][1])
                nbr_source_to = nbr_source + int(almanac[almanac_names[x]][i][2]) - 1

def main():
    almanac = init_almanac()

    #print(get_min_location(almanac, almanac["seeds"]))
    pprint(almanac)

if __name__ == "__main__":
    main()
