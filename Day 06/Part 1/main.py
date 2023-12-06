# Advent of Code 2023 - Day 6 - Part 1
# https://adventofcode.com/2023/day/6#part1

def get_nbr_ways(time, distance):
    nbr_ways = 0

    for i in range(int(time) + 1):
        rest = int(time) - i
        d = rest * i

        if d > int(distance):
            nbr_ways += 1

    return nbr_ways

def multiply_list(lst):
    result = 1

    for num in lst:
        result *= num

    return result

def main():
    all_ways = []

    with open("Day 06/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line.split(":") for line in lines]

    times = [time for time in lines[0][1].split(" ") if time]
    distances = [distance for distance in lines[1][1].split(" ") if distance]

    for i in range(len(times)):
        all_ways.append(get_nbr_ways(times[i], distances[i]))

    print(multiply_list(all_ways))

if __name__ == "__main__":
    main()
