# A rock, B = Paper, C = Scissors
# X = rock, Y = Paper, Z = Scissors
ROCK, PAPER, SCISSORS = 1, 2, 3

WINS = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
LOSES = {v: k for k, v in WINS.items()}


def parse_input(file):
    result = []
    with open(file) as in_file:
        result.extend(tuple(line.strip().split()) for line in in_file)
    return result


def match_result(elf, you):
    if WINS[you] == elf:
        return 6
    elif elf == you:
        return 3
    return 0


def part_one(strategy):
    score = 0
    for elf, you in strategy:
        _elf = ord(elf) - ord("@")
        _you = ord(you) - ord("@") - (ord("X") - ord("A"))
        score += _you + match_result(_elf, _you)

    return score


def part_two(strategy):
    score = 0
    for elf, you in strategy:
        _elf = ord(elf) - ord("@")
        if you == "X":
            score += 0 + WINS[_elf]
        elif you == "Y":
            score += 3 + _elf
        else:
            score += 6 + LOSES[_elf]

    return score


if __name__ == "__main__":
    strategy = parse_input("input.txt")
    print(f"Part 1: {part_one(strategy)}")
    print(f"Part 2: {part_two(strategy)}")
