# Advent of Code 2023 - Day 5 - Part 2
# https://adventofcode.com/2023/day/5#part2

def get_min_location(almanac, seeds_pairs):
    min_location = None

    for i in range(0, len(seeds_pairs) - 1, 2):
        for x in range(int(seeds_pairs[i]), int(seeds_pairs[i]) + int(seeds_pairs[i + 1]) - 1):
            location = get_location(almanac, str(x))

            if (min_location == None or int(location) < min_location):
                min_location = int(location)

    return min_location

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

    almanac[almanac_names[almanac_nbr]] = lines[0][1:]

    while (i < len(lines)):
        if (lines[i] == []):
            almanac_nbr += 1
            i += 2
            continue
        almanac[almanac_names[almanac_nbr]].append(lines[i])
        i += 1

    return almanac

def get_location(almanac, seed):
    almanac_names = ["soil", "fertilizer", "water", "light", "temperature", "humidity", "location"]
    source = seed

    for x in range(len(almanac_names)):
        for i in range(len(almanac[almanac_names[x]])):
            nbr_destination = int(almanac[almanac_names[x]][i][0])
            nbr_source = int(almanac[almanac_names[x]][i][1])
            nbr_range = int(almanac[almanac_names[x]][i][2])

            if (((nbr_source) <= int(source)) and ((nbr_source + nbr_range - 1) >= int(source))):
                source = str(nbr_destination + int(source) - nbr_source)
                break

    return source

def main():
    almanac = init_almanac()

    print(get_min_location(almanac, almanac["seeds"]))

if __name__ == "__main__":
    main()
