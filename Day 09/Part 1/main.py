# Advent of Code 2023 - Day 9 - Part 1
# https://adventofcode.com/2023/day/9#part1

def last_sequence(numbers):
    for c in numbers:
        if c != 0:
            return False

    return True

def get_extrapolated_value(sequences):
    keys = list(sequences.keys())
    last_key = keys[-1]
    i = int(last_key) - 1

    sequences[last_key].append(0)

    while i > 1:
        sequences[str(i)].append(sequences[str(i)][-1] + sequences[str(i + 1)][-1])
        i -= 1

    return sequences["1"][-1] + sequences["2"][-1]

def get_all_sequences(line):
    all_numbers = [int(number) for number in line.split(" ")]
    sequences = {}
    sequences["1"] = all_numbers
    i = 2

    while True:
        new_sequence = []
        index = -2

        for nbr in reversed(sequences[str(i - 1)]):
            if index < -len(sequences[str(i - 1)]):
                break
            new_sequence.append(nbr - sequences[str(i - 1)][index])
            index -= 1

        new_sequence.reverse()
        sequences[str(i)] = new_sequence

        if last_sequence(new_sequence):
            break

        i += 1

    return sequences

def main():
    extrapolated_values = []

    with open("Day 09/puzzle_input.txt", "r") as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines]

    for line in lines:
        extrapolated_values.append(get_extrapolated_value(get_all_sequences(line)))

    print(sum(extrapolated_values))

if __name__ == "__main__":
    main()
