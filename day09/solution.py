class Position:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == "U":
            self.y += 1
        elif direction == "D":
            self.y -= 1
        elif direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1

    def touches(self, other):
        return abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1

    def close_gap(self, other):
        if self.y < other.y:
            self.move("U")
        elif self.y > other.y:
            self.move("D")
        if self.x < other.x:
            self.move("R")
        elif self.x > other.x:
            self.move("L")

    def __str__(self):
        return f"{self.x}, {self.y}"

    def __repr__(self):
        return str(self)


def parse_input():
    moves = []
    with open("input.txt") as in_file:
        moves.extend(line.strip().split(" ") for line in in_file)
    return moves


def part_one(moves):
    head = Position(0, 0)
    tail = Position(0, 0)
    tail_visited = set()
    for move in moves:
        direction = move[0]
        steps = int(move[1])
        while steps > 0:
            head.move(direction)
            if not tail.touches(head):
                tail.close_gap(head)
            if str(tail) not in tail_visited:
                tail_visited.add(str(tail))
            steps -= 1
    return len(tail_visited)


def part_two(moves):
    knots = [Position(0, 0) for _ in range(10)]
    t_visited = set()
    for move in moves:
        direction = move[0]
        steps = int(move[1])
        while steps > 0:
            knots[0].move(direction)
            for i in range(1, 10):
                if not knots[i].touches(knots[i - 1]):
                    knots[i].close_gap(knots[i - 1])
                if i == 9 and str(knots[i] not in t_visited):
                    t_visited.add(str(knots[i]))
            steps -= 1
    return len(t_visited)


if __name__ == "__main__":
    moves = parse_input()
    print(f"Part 1: {part_one(moves)}")
    print(f"Part 2: {part_two(moves)}")
