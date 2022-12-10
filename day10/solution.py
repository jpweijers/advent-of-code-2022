from dataclasses import dataclass, field
from typing import List


def parse_input():
    with open("input.txt") as f:
        return [line.strip() for line in f]


def part_one(lines):
    def add_to_result(x, cycles):
        nonlocal result
        if cycles in measure_at:
            result += x * cycles

    result = 0
    x = 1
    measure_at = {20, 60, 100, 140, 180, 220}
    cycles = 0

    for line in lines:
        action = line.split()[0]
        if action == "noop":
            cycles += 1
            add_to_result(x, cycles)
        if action == "addx":
            cycles += 1
            add_to_result(x, cycles)
            cycles += 1
            add_to_result(x, cycles)
            x += int(line.split()[1])

    return result


def part_two(lines):
    @dataclass
    class Crt:
        x: int = 1
        screen: List[str] = field(default_factory=lambda: [" "] * 240)

        def write(self, cycles):
            if abs(self.x - (cycles - 1) % 40) <= 1:
                self.screen[cycles - 1] = "#"

        def render(self):
            screen = "".join(self.screen)
            return "".join(screen[i * 40 : (i + 1) * 40] + "\n" for i in range(6))

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
