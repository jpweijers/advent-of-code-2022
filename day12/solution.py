from search import dfs, node_to_path
from typing import NamedTuple



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
        self.rows = 0
        self.cols = 0
        self.grid = []
        self.start = None
        self.goal = None

    def __str__(self):
        output = ""
        for row in self.grid:
            output += "".join([str(square) for square in row]) + "\n"
        return output

    def move_options(self, location: Location):
        locations = []

        if location.row + 1 < self.rows and (
            abs(
                self.grid[location.row + 1][location.col].height
                - self.grid[location.row][location.col].height
            )
            <= 1
            or location == self.start
            or Location(location.row + 1, location.col) == self.goal
        ):
            locations.append(Location(location.row + 1, location.col))
        if location.row >= 1 and (
            abs(
                self.grid[location.row - 1][location.col].height
                - self.grid[location.row][location.col].height
            )
            <= 1
            or location == self.start
            or Location(location.row - 1, location.col) == self.goal
        ):
            locations.append(Location(location.row - 1, location.col))
        if location.col + 1 < self.cols and (
            abs(
                self.grid[location.row][location.col + 1].height
                - self.grid[location.row][location.col].height
            )
            <= 1
            or location == self.start
            or Location(location.row, location.col + 1) == self.goal
        ):
            locations.append(Location(location.row, location.col + 1))
        if location.col >= 1 and (
            abs(
                self.grid[location.row][location.col - 1].height
                - self.grid[location.row][location.col].height
            )
            <= 1
            or location == self.start
            or Location(location.row, location.col - 1) == self.goal
        ):
            locations.append(Location(location.row, location.col - 1))
        return locations

    def goal_test(self, location: Location):
        return location == self.goal


def parse_input():
    grid = Grid()
    with open("test_input.txt") as f:
        for line in f:
            line = line.strip()
            grid.rows += 1
            grid.cols = max(len(line), grid.cols)
            for c in line:
                if c == "S":
                    grid.start = Location(grid.rows - 1, line.index(c))
                elif c == "E":
                    grid.goal = Location(grid.rows - 1, line.index(c))
            grid.grid.append([Square(ord(c)) for c in line])
    return grid


def part_one():
    grid = parse_input()
    print(grid)
    solution = dfs(grid.start, grid.goal_test, grid.move_options)
    print(solution)
    path = node_to_path(solution)
    print(len(path))


def part_two():
    pass


if __name__ == "__main__":
    print(f"Part 1: {part_one()}")
    print(f"Part 2: {part_two()}")
