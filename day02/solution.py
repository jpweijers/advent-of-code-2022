import re

# A rock, B = Paper, C = Scissors
# X = rock, Y = Paper, Z = Scissors
A, B, C = 1, 2, 3
BEATS = {A: C, B: A, C: B}
LOSES = {v: k for k, v in BEATS.items()}


def parse_input(file):
    result = []
    with open(file) as in_file:
        for line in in_file:
            splitted = re.split(r"\s", line)
            result.append((splitted[0], splitted[1]))
    return result


def part_one(strategy):
    score = 0
    for elf, you in strategy:
        _elf = ord(elf) - ord("@")
        _you = ord(you) - ord("@") - (ord("X") - ord("A"))
        if _elf == _you:
            score += 3 + _you
        elif BEATS[_you] == _elf:
            score += 6 + _you
        else:
            score += 0 + _you
    print(score)


def part_two(strategy):
    score = 0
    for elf, you in strategy:
        _elf = ord(elf) - ord("@")
        if you == "X":
            score += 0 + BEATS[_elf]
        elif you == "Y":
            score += 3 + _elf
        else:
            score += 6 + LOSES[_elf]

    print(score)


if __name__ == "__main__":
    strategy = parse_input("input.txt")
    part_one(strategy)
    part_two(strategy)
