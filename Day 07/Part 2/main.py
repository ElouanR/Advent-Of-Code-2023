# Advent of Code 2023 - Day 7 - Part 2
# https://adventofcode.com/2023/day/7#part2

def is_oneP(line):
    char_counts = {}
    joker_count = line.count('J')

    for char in line:
        if char != 'J':
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    for char in char_counts:
        if char_counts[char] == 1 and joker_count > 0:
            char_counts[char] += 1
            joker_count -= 1

    result = list(char_counts.values()).count(2) == 1 and list(char_counts.values()).count(1) == 3

    return result

def is_twoP(line):
    char_counts = {}
    joker_count = line.count('J')

    for char in line:
        if char != 'J':
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    for char in char_counts:
        if char_counts[char] == 1 and joker_count > 0:
            char_counts[char] += 1
            joker_count -= 1

    result = list(char_counts.values()).count(2) == 2 and list(char_counts.values()).count(1) == 1

    return result

def is_threeK(line):
    char_counts = {}
    joker_count = line.count('J')

    for char in line:
        if char != 'J':
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    for char in char_counts:
        if char_counts[char] < 3 and joker_count > 0:
            joker_needed = 3 - char_counts[char]
            if joker_needed <= joker_count:
                char_counts[char] += joker_needed
                joker_count -= joker_needed

    result = 3 in char_counts.values() and 1 in char_counts.values() and len(char_counts) == 3

    return result

def is_fullH(line):
    char_counts = {}
    joker_count = line.count('J')

    for char in line:
        if char != 'J':
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    for char in char_counts:
        if char_counts[char] < 3 and joker_count > 0:
            joker_needed = 3 - char_counts[char]
            if joker_needed <= joker_count:
                char_counts[char] += joker_needed
                joker_count -= joker_needed

    if 2 not in char_counts.values() and joker_count == 2:
        char_counts['J'] = 2
        joker_count -= 2

    result = 3 in char_counts.values() and 2 in char_counts.values()

    return result

def is_fourK(line):
    char_counts = {}
    joker_count = line.count('J')

    for char in line:
        if char != 'J':
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    for char in char_counts:
        if char_counts[char] < 4 and joker_count > 0:
            joker_needed = 4 - char_counts[char]
            if joker_needed <= joker_count:
                char_counts[char] += joker_needed
                joker_count -= joker_needed

    result = 4 in char_counts.values() and 1 in char_counts.values()

    return result

def is_fiveK(line):
    char_counts = {}
    joker_count = line.count('J')

    for char in line:
        if char != 'J':
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    for char in char_counts:
        if char_counts[char] < 5 and joker_count > 0:
            joker_needed = 5 - char_counts[char]
            if joker_needed <= joker_count:
                char_counts[char] += joker_needed
                joker_count -= joker_needed

    if joker_count == 5:
        char_counts['J'] = 5
        joker_count -= 5

    result = 5 in char_counts.values()

    return result

def get_hand_types(hand_types, lines):
    for line in lines:
        if (is_fiveK(line[0])):
            hand_types["fiveK"].append(line)
            continue
        if (is_fourK(line[0])):
            hand_types["fourK"].append(line)
            continue
        if (is_fullH(line[0])):
            hand_types["fullH"].append(line)
            continue
        if (is_threeK(line[0])):
            hand_types["threeK"].append(line)
            continue
        if (is_twoP(line[0])):
            hand_types["twoP"].append(line)
            continue
        if (is_oneP(line[0])):
            hand_types["oneP"].append(line)
            continue
        if (len(set(line[0])) == 5 and line[0].count('J') == 0):
            hand_types["highC"].append(line)
            continue

    return hand_types

def power_key(x):
    power = {'A': 14, 'K': 13, 'Q': 12, 'T': 11, '9': 10, '8': 9, '7': 8, '6': 7, '5': 6, '4': 5, '3': 4, '2': 3, 'J': 2}

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
