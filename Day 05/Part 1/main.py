# Advent of Code 2023 - Day 5 - Part 1
# https://adventofcode.com/2023/day/5#part1

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
    all_locations = []

    for i in range(len(almanac["seeds"])):
        all_locations.append(get_location(almanac, almanac["seeds"][i]))

    for i in range(len(all_locations)):
        all_locations[i] = int(all_locations[i])

    print(min(all_locations))

if __name__ == "__main__":
    main()
