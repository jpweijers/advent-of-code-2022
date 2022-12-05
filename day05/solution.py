import re
from copy import deepcopy
from dataclasses import dataclass
from typing import List


@dataclass
class Move:
    amount: int
    _from: int
    to: int


def parse_input(file_name: str) -> tuple[List[Move], dict]:
    moves = []
    with open(file_name) as in_file:
        for line in in_file:
            _match = re.findall(r"move (\d+) from (\d+) to (\d+)", line)[0]
            _match = [int(m) for m in _match]
            moves.append(Move(_match[0], _match[1], _match[2]))

    with open("crates.txt") as in_file:
        crates = {i: [] for i in range(1, 10)}
        for line in in_file.readlines()[:-1]:
            stacks = []
            for i in range(0, len(line), len(line) // 9):
                s = re.findall(r"\w", line[i : i + 4])
                stacks.append(s)
            for i, stack in enumerate(stacks, start=1):
                crates[i] = stack + crates[i]

    return (moves, crates)


def part_1(crates: dict, moves: List[Move]) -> str:
    _crates = deepcopy(crates)
    for move in moves:
        for _ in range(move.amount):
            item = _crates[move._from].pop()
            _crates[move.to].append(item)

    return "".join([v[-1] for k, v in _crates.items()])


def part_2(crates: dict, moves: List[Move]) -> str:
    _crates = deepcopy(crates)
    for move in moves:
        items = _crates[move._from][-move.amount :]
        del _crates[move._from][-move.amount :]
        _crates[move.to] += items

    return "".join([v[-1] for k, v in _crates.items()])


if __name__ == "__main__":
    moves, crates = parse_input("moves.txt")
    print(f"Part 1: {part_1(crates, moves)}")
    print(f"Part 2: {part_2(crates, moves)}")
