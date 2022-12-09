def parse_input():
    with open("./input.txt") as infile:
        return [line.strip() for line in infile]


def calories_per_elf(calories):
    totals = []
    subtotal = 0
    for calorie in calories:
        if calorie == "":
            totals.append(subtotal)
            subtotal = 0
        else:
            subtotal += int(calorie)

    return sorted(totals, reverse=True)


if __name__ == "__main__":
    calories = parse_input()
    totals = calories_per_elf(calories)
    print(f"answer part 1: {calories_per_elf(calories)[0]}")
    print(f"answer part 2: {sum(totals[:3])}")
