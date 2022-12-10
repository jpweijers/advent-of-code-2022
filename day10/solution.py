def parse_input():
    with open("input.txt") as f:
        return [line.strip() for line in f]


def part_one(lines):
    x = 1
    value = 0
    measure_at = [20, 60, 100, 140, 180, 220]
    cycles = 1
    addx = 0
    i = 0
    action = lines[0].split()[0]
    while cycles <= 221:
        if cycles in measure_at:
            print(f"cycles: {cycles}, x: {x}")
            value += x * cycles
        if action == "noop":
            i += 1
            action = lines[i].split()[0]
            if action == "addx":
                addx = 0
        elif action == "addx" and addx < 1:
            addx += 1
        else:
            x += int(lines[i].split()[1])
            i += 1
            action = lines[i].split()[0]
            if action == "addx":
                addx = 0
        cycles += 1
    return value


class Crt:
    def __init__(self):
        self.x = 1
        self.screen = ["."] * 240

    def write(self, cycles):
        print(f"cycle: {cycles}, x: {self.x}, diff: {abs(self.x - cycles-1 % 40)})")
        self.screen[cycles - 1] = "#" if abs(self.x - (cycles - 1) % 40) <= 1 else " "

    def render(self):
        return "".join(
            "".join(self.screen[i * 40 : (i + 1) * 40]) + "\n" for i in range(6)
        )


def part_two(lines):
    crt = Crt()
    cycles = 1

    for line in lines:
        action = line.split()[0]
        if action == "noop":
            crt.write(cycles)
            cycles += 1

        elif action == "addx":
            crt.write(cycles)
            cycles += 1
            crt.write(cycles)
            cycles += 1

            crt.x += int(line.split()[1])

    return crt.render()


if __name__ == "__main__":
    lines = parse_input()
    print(f"Part one: {part_one(lines)}")
    print(f"Part two: \n{part_two(lines)}")
