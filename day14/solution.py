class PathNode:
    def __init__(self, x: int, y: int, parent=None):
        self.x = x
        self.y = y
        self.parent: object = parent

    def __repr__(self):
        return f"PathNode({self.x}, {self.y}, {self.parent})"


class Grid:
    def __init__(self, height=500, width=500):
        self.min_y = height
        self.max_y = height
        self.min_x = width
        self.max_x = width
        self.grid = [[]]

    def set_grid(self):
        self.grid = [
            ["." for _ in range(self.max_y + 1)] for _ in range(self.max_x + 1)
        ]

    def add_floor(self):
        floor = ["#"] * self.max_y
        self.grid.append(floor)

    def draw_path(self, path):
        while path.parent:
            if path.x == path.parent.x:
                for y in range(
                    min(path.y, path.parent.y), max(path.y, path.parent.y) + 1
                ):
                    self.grid[path.x][y] = "#"
            elif path.y == path.parent.y:
                for x in range(
                    min(path.x, path.parent.x), max(path.x, path.parent.x) + 1
                ):
                    self.grid[x][path.y] = "#"
                    self.grid[x][path.y] = "#"

            path = path.parent

    def drop_sand(self, floor=False) -> bool:
        sand_x, sand_y = 500, 0

        while True:
            if self.grid[sand_x][sand_y + 1] == ".":
                sand_y += 1
            elif self.grid[sand_x - 1][sand_y + 1] == ".":
                sand_x = max(0, sand_x - 1)
                sand_y += 1
            elif self.grid[sand_x + 1][sand_y + 1] == ".":
                sand_x = min(self.max_x - 1, sand_x + 1)
                sand_y += 1
            else:
                self.grid[sand_x][sand_y] = "o"
                return True

            if floor and sand_y == self.max_y - 1:
                print(f"floor: {sand_x}, {sand_y}")
                return True
                
            elif sand_y >= self.max_y:
                return False



    def __repr__(self):
        grid = ""
        for x in range(self.min_x, len(self.grid)):
            for y in range(self.min_y, len(self.grid[x])):
                grid += self.grid[x][y]
            grid += "\n"
        return grid


def parse_input():
    paths = []
    grid = Grid()
    with open("input.txt") as f:
        for line in f:
            nodes = line.strip().split("->")
            x, y = nodes[0].strip().split(",")
            path = PathNode(int(x), int(y))
            for i in range(1, len(nodes)):
                x, y = nodes[i].strip().split(",")
                grid.max_y = max(grid.max_y, int(y))
                grid.min_y = min(grid.min_y, int(y))
                grid.max_x = max(grid.max_x, int(x))
                grid.min_x = min(grid.min_x, int(x))

                path = PathNode(int(x), int(y), path)

            paths.append(path)
    return paths, grid


def part_one():
    paths, grid = parse_input()
    grid.set_grid()

    for path in paths:
        grid.draw_path(path)

    sand_count = 0
    while True:
        if grid.drop_sand():
            sand_count += 1
        else:
            return sand_count


def part_two():
    paths, grid = parse_input()
    grid.set_grid()

    for path in paths:
        grid.draw_path(path)

    sand_count = 0
    grid.max_y += 2
    while True:
        if grid.drop_sand(floor=True):
            sand_count += 1
            print(sand_count)
        else:
            return sand_count


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
