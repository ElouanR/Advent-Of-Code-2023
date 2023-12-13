# Advent of Code 2023 - Day 5 - Part 2
# https://adventofcode.com/2023/day/5#part2

from pprint import pprint

def get_min_location(almanac, seeds_ranges):
    for seeds in seeds_ranges:
        tmp = []
        tmp.append(seeds)
        tmp[0][0] = int(tmp[0][0])
        tmp[0][1] = int(tmp[0][1])
        get_location(almanac, tmp)

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
        tmp = []
        while sources_range != []:
            for i in range(len(almanac[almanac_names[x]])):
                nbr_destination = int(almanac[almanac_names[x]][i][0])
                nbr_source = int(almanac[almanac_names[x]][i][1])
                nbr_source_to = nbr_source + int(almanac[almanac_names[x]][i][2]) - 1
                seeds_to = sources_range[0][0] + sources_range[0][1] - 1

                overlap_point_start = max(nbr_source, sources_range[0][0])
                overlap_point_end = min(nbr_source_to, seeds_to)

                print(sources_range)
                print(seeds_to)
                print()
                print("nbr_source: ", nbr_source)
                print("nbr_source_to: ", nbr_source_to)
                print()
                print("overlap_point_start: ", overlap_point_start)
                print("overlap_point_end: ", overlap_point_end)
                print()

                if (nbr_source <= sources_range[0][0] and nbr_source_to >= seeds_to):
                    print("source_range in destination_range")

                if (nbr_source > sources_range[0][0] and nbr_source_to < seeds_to):
                    print("destination_range in source_range")

                input()

def main():
    almanac = init_almanac()

    get_min_location(almanac, almanac["seeds"])
    #pprint(almanac)

if __name__ == "__main__":
    main()
