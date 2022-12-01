if __name__ == "__main__":
    with open("./input.txt") as infile:
        _max = 0
        subtotal = 0
        totals = []
        for line in infile:
            if line == "\n":
                _max = max(_max, subtotal)
                totals.append(subtotal)
                subtotal = 0
            else:
                subtotal += int(line)
    totals.sort()

    print(f"answer part 1: {_max}")
    print(f"answer part 2: {sum(totals[-3:])}")
