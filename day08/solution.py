import itertools


def parse_input():
    with open("input.txt") as in_file:
        grid = []
        for line in in_file:
            line = line.strip()
            grid.append([int(h) for h in line])

        return grid


def part_one(grid):
    visible = 0

    for row, col in itertools.product(range(len(grid)), range(len(grid))):
        tree = grid[row][col]
        if row == 0 or col == 0 or row == len(grid) - 1 or col == len(grid) - 1:
            visible += 1
            continue
        if tree > max(grid[row][c] for c in range(col)):
            visible += 1
            continue
        if tree > max(grid[row][c] for c in range(col + 1, len(grid))):
            visible += 1
            continue
        if tree > max(grid[r][col] for r in range(row)):
            visible += 1
            continue
        if tree > max(grid[r][col] for r in range(row + 1, len(grid))):
            visible += 1
    return visible


def part_two(grid):
    _max = 0
    for row, col in itertools.product(range(len(grid)), range(len(grid))):
        tree = grid[row][col]
        left, right, up, down = (0 for _ in range(4))
        for c in range(col - 1, -1, -1):
            left += 1
            if grid[row][c] >= tree:
                break
        for c in range(col + 1, len(grid)):
            right += 1
            if grid[row][c] >= tree:
                break
        for r in range(row - 1, -1, -1):
            up += 1
            if grid[r][col] >= tree:
                break
        for r in range(row + 1, len(grid)):
            down += 1
            if grid[r][col] >= tree:
                break
        _max = max(_max, left * right * up * down)

    return _max


if __name__ == "__main__":
    grid = parse_input()
    print(f"Part 1: {part_one(grid)}")
    print(f"Part 2: {part_two(grid)}")
