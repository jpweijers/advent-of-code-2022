import numpy as np


class Monkey:
    def __init__(self, items, operation, test, recipients):
        self.inspections = 0
        self.items = items
        self.operation = operation
        self.test = test
        self.recipients = recipients

    def operate(self, num):
        r = self.operation
        return eval(r.replace("old", str(num)))

    def total(self):
        return sum(self.items)

    def __repr__(self):
        return f"Monkey({self.items}, {self.operation}, {self.test}, {self.recipients})"


def read_input():
    monkeys = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()

            if line.startswith("Monkey"):
                monkeys.append(Monkey([], 0, 0, []))

            if line.startswith("Starting items: "):
                monkeys[-1].items = [int(x) for x in line.split(":")[1].split(", ")]

            if line.startswith("Operation: "):
                monkeys[-1].operation = line.split("= ")[1]

            if line.startswith("Test: "):
                monkeys[-1].test = int(line.split("Test: divisible by ")[1])

            if line.startswith("If "):
                monkeys[-1].recipients.append(int(line.split("monkey ")[1]))

    return monkeys


def part_one():
    monkeys = read_input()

    for round in range(20):
        print(round + 1)
        for monkey in monkeys:
            while monkey.items:
                num = monkey.items.pop(0)
                num = monkey.operate(num)
                num = num // 3
                if num % monkey.test == 0:
                    monkeys[monkey.recipients[0]].items.append(num)
                else:
                    monkeys[monkey.recipients[1]].items.append(num)
                monkey.inspections += 1

    monkeys.sort(key=lambda m: m.inspections, reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections


def part_two():
    monkeys = read_input()

    modulo = 1
    for m in monkeys:
        modulo *= m.test

    for _ in range(10000):
        for monkey in monkeys:
            while monkey.items:
                num = monkey.items.pop(0)
                num = monkey.operate(num)
                num = num % modulo
                if num % monkey.test == 0:
                    monkeys[monkey.recipients[0]].items.append(num)
                else:
                    monkeys[monkey.recipients[1]].items.append(num)
                monkey.inspections += 1

    monkeys.sort(key=lambda m: m.inspections, reverse=True)
    return monkeys[0].inspections * monkeys[1].inspections


if __name__ == "__main__":
    print(f"Part one: {part_one()}")  # 120384
    print(f"Part two: {part_two()}")  # 32059801242
