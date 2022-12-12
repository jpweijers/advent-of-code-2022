from typing import NamedTuple

from search import astar, bfs, dfs, node_to_path


class Square:
    def __init__(self, height):
        self.height = height

    def __str__(self):
        return chr(self.height)

    def __repr__(self):
        return chr(self.height)


class Location(NamedTuple):
    row: int
    col: int


class Grid:
    def __init__(self):
        self.grid = []
        self.start = None
        self.goal = None

    def __str__(self):
        return "".join(
            "".join([str(square) for square in row]) + "\n" for row in self.grid
        )

    def move_options(self, location: Location):
        locations = []

        UP = Location(location.row - 1, location.col)
        DOWN = Location(location.row + 1, location.col)
        LEFT = Location(location.row, location.col - 1)
        RIGHT = Location(location.row, location.col + 1)

        height = self.grid[location.row][location.col].height

        if UP.row >= 0 and height + 1 >= self.grid[UP.row][UP.col].height:
            locations.append(UP)
        if (
            DOWN.row < len(self.grid)
            and height + 1 >= self.grid[DOWN.row][DOWN.col].height
        ):
            locations.append(DOWN)
        if LEFT.col >= 0 and height + 1 >= self.grid[LEFT.row][LEFT.col].height:
            locations.append(LEFT)
        if (
            RIGHT.col < len(self.grid[0])
            and height + 1 >= self.grid[RIGHT.row][RIGHT.col].height
        ):
            locations.append(RIGHT)

        return locations

    def goal_test(self, location: Location):
        return location == self.goal

    def mark(self, path):
        for i, location in enumerate(path):
            if i < len(path) - 1:
                parent = path[i + 1]
                if location.row > parent.row:
                    self.grid[location.row][location.col] = Square(ord("^"))
                elif location.row < parent.row:
                    self.grid[location.row][location.col] = Square(ord("V"))
                elif location.col > parent.col:
                    self.grid[location.row][location.col] = Square(ord("<"))
                elif location.col < parent.col:
                    self.grid[location.row][location.col] = Square(ord(">"))
            else:
                self.grid[location.row][location.col] = Square(ord("S"))


def parse_input():
    grid = Grid()
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            for c in line:
                if c == "E":
                    grid.goal = Location(len(grid.grid), line.index(c))
                if c == "S":
                    grid.start = Location(len(grid.grid), line.index(c))
            line = line.replace("S", "a")
            line = line.replace("E", "z")
            grid.grid.append([Square(ord(c)) for c in line])
    return grid


def part_one():
    grid = parse_input()
    if solution := astar(grid.start, grid.goal_test, grid.move_options):
        path = node_to_path(solution)
        grid.mark(path)
        # print(grid)
        return solution.cost
    return float("inf")


def part_two():
    grid = parse_input()
    starts = []
    for row in range(len(grid.grid)):
        for col in range(len(grid.grid[0])):
            if grid.grid[row][col].height == ord("a"):
                starts.append(Location(row, col))

    result = float("inf")

    for start in starts:
        grid.start = start
        if solution := astar(grid.start, grid.goal_test, grid.move_options):
            result = min(result, solution.cost)
    return result


if __name__ == "__main__":
    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")
