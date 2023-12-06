# Advent of Code 2023 - Day 6 - Part 2
# https://adventofcode.com/2023/day/6#part2

def get_nbr_ways(time, distance):
    nbr_ways = 0

    for i in range(int(time) + 1):
        rest = int(time) - i
        d = rest * i

        if d > int(distance):
            nbr_ways += 1

    return nbr_ways

def main():
    all_ways = None

    with open("Day 06/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line.split(":") for line in lines]

    times = [time for time in lines[0][1].split(" ") if time]
    time = ''.join(times)
    distances = [distance for distance in lines[1][1].split(" ") if distance]
    distance = ''.join(distances)

    all_ways = get_nbr_ways(time, distance)

    print(all_ways)

if __name__ == "__main__":
    main()
