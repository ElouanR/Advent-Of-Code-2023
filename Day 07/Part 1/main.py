# Advent of Code 2023 - Day 7 - Part 1
# https://adventofcode.com/2023/day/7#part1

def is_oneP(line):
    char_counts = {}

    for char in line:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    result = list(char_counts.values()).count(2) == 1 and list(char_counts.values()).count(1) == 3

    return result

def is_twoP(line):
    char_counts = {}

    for char in line:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    result = list(char_counts.values()).count(2) == 2 and list(char_counts.values()).count(1) == 1

    return result

def is_threeK(line):
    char_counts = {}

    for char in line:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    result = 3 in char_counts.values() and 1 in char_counts.values() and len(char_counts) == 3

    return result

def is_fullH(line):
    char_counts = {}

    for char in line:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    result = 3 in char_counts.values() and 2 in char_counts.values()

    return result

def is_fourK(line):
    char_counts = {}

    for char in line:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    result = 4 in char_counts.values() and 1 in char_counts.values()

    return result

def get_highC(hand_types, lines):
    for line in lines:
        if (len(set(line[0])) == 5):
            hand_types["highC"].append(line)

    return hand_types

def get_oneP(hand_types, lines):
    for line in lines:
        if (is_oneP(line[0])):
            hand_types["oneP"].append(line)

    return hand_types

def get_twoP(hand_types, lines):
    for line in lines:
        if (is_twoP(line[0])):
            hand_types["twoP"].append(line)

    return hand_types

def get_threeK(hand_types, lines):
    for line in lines:
        if (is_threeK(line[0])):
            hand_types["threeK"].append(line)

    return hand_types

def get_fullH(hand_types, lines):
    for line in lines:
        if (is_fullH(line[0])):
            hand_types["fullH"].append(line)

    return hand_types

def get_fourK(hand_types, lines):
    for line in lines:
        if (is_fourK(line[0])):
            hand_types["fourK"].append(line)

    return hand_types

def get_fiveK(hand_types, lines):
    for line in lines:
        if (len(set(line[0])) == 1):
            hand_types["fiveK"].append(line)

    return hand_types

def get_hand_types(hand_types, lines):
    hand_types = get_highC(hand_types, lines)
    hand_types = get_oneP(hand_types, lines)
    hand_types = get_twoP(hand_types, lines)
    hand_types = get_threeK(hand_types, lines)
    hand_types = get_fullH(hand_types, lines)
    hand_types = get_fourK(hand_types, lines)
    hand_types = get_fiveK(hand_types, lines)

    return hand_types

def power_key(x):
    power = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}

    return tuple(power[i] for i in x[0])

def sort_hand_types(hand_types):
    hand_types["fiveK"] = sorted(hand_types["fiveK"], key=power_key)
    hand_types["fourK"] = sorted(hand_types["fourK"], key=power_key)
    hand_types["fullH"] = sorted(hand_types["fullH"], key=power_key)
    hand_types["threeK"] = sorted(hand_types["threeK"], key=power_key)
    hand_types["twoP"] = sorted(hand_types["twoP"], key=power_key)
    hand_types["oneP"] = sorted(hand_types["oneP"], key=power_key)
    hand_types["highC"] = sorted(hand_types["highC"], key=power_key)

    return hand_types

def get_totalw(hand_types):
    totalw = 0
    rank = 1

    for key in hand_types:
        for line in hand_types[key]:
            totalw += rank * int(line[1])
            rank += 1

    return totalw

def main():
    hand_types = {
        "highC": [],
        "oneP": [],
        "twoP": [],
        "threeK": [],
        "fullH": [],
        "fourK": [],
        "fiveK": []
    }

    with open("Day 07/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]
    lines = [line.split(" ") for line in lines]

    hand_types = get_hand_types(hand_types, lines)
    hand_types = sort_hand_types(hand_types)

    print(get_totalw(hand_types))

if __name__ == "__main__":
    main()
