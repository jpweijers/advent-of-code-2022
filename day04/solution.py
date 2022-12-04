from dataclasses import dataclass


@dataclass
class Elf:
    start: int
    end: int


@dataclass
class Pair:
    first: Elf
    second: Elf


def parse_input(file):
    pairs = []
    with open(file) as in_file:
        for line in in_file:
            sections = line.strip().split(",")

            first = sections[0].split("-")
            second = sections[1].split("-")
            pairs.append(
                Pair(
                    Elf(int(first[0]), int(first[1])),
                    Elf(int(second[0]), int(second[1])),
                )
            )

    return pairs


def part_1(pairs):
    return sum(
        pair.first.start >= pair.second.start
        and pair.first.end <= pair.second.end
        or pair.second.start >= pair.first.start
        and pair.second.end <= pair.first.end
        for pair in pairs
    )


def part_2(pairs):
    return sum(
        pair.first.start <= pair.second.start <= pair.first.end
        or pair.second.start <= pair.first.start <= pair.second.end
        or pair.first.start <= pair.second.end <= pair.first.end
        or pair.second.start <= pair.first.end <= pair.second.end
        for pair in pairs
    )


if __name__ == "__main__":
    pairs = parse_input("input.txt")
    print(f"Part 1: {part_1(pairs)}")
    print(f"Part 2: {part_2(pairs)}")
