def parse_input(file):
    result = []
    with open(file) as rucksacks:
        for rucksack in rucksacks:
            compartments = rucksack.strip()
            first = slice(0, len(compartments) // 2)
            second = slice(len(compartments) // 2, len(compartments))
            result.append((compartments[first], compartments[second]))

    return result


score_map = {}
for i in range(1, 27):
    score_map[chr(i + 96)] = i

for i in range(27, 53):
    score_map[chr(i + 38)] = i


def part_1(rucksacks):
    result = 0
    for comp1, comp2 in rucksacks:
        for item in comp1:
            if item in comp2:
                result += score_map[item]
                break

    return result


def part_2(rucksacks):
    rucksack_groups = []
    for i in range(0, len(rucksacks), 3):
        rucksack_groups.append(tuple(c1 + c2 for c1, c2 in rucksacks[i : i + 3]))

    result = 0
    for comp1, comp2, comp3 in rucksack_groups:
        for item in comp1:
            if item in comp2 and item in comp3:
                result += score_map[item]
                break
    return result


if __name__ == "__main__":
    rucksacks = parse_input("input.txt")
    print(f"Part 1: {part_1(rucksacks)}")
    print(f"Part 2: {part_2(rucksacks)}")
