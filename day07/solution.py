import re

from anytree import AsciiStyle, NodeMixin, PostOrderIter, RenderTree


class Node(NodeMixin):
    def __init__(self, name, size, parent=None, children=None):
        super(Node, self).__init__()
        self.name = name
        self.size = size
        self.parent = parent
        if children:
            self.children = children

    def get_size(self):
        return self.size + sum(child.get_size() for child in self.children)

    def __repr__(self):
        return f"{self.name} - {self.get_size()}"


def parse_input():
    root = cwd = Node("/", 0)
    with open("input.txt") as in_file:
        for line in in_file:
            line = line.strip()
            if line[:4] == "$ cd":
                _dir = line[5:]
                if _dir == "..":
                    cwd = cwd.parent
                else:
                    cwd = Node(_dir, 0, cwd)
            elif re.match(r"\d+\s\w+", line):
                size = line.split()[0]
                cwd.size += int(size)

    return root.children[0]


def write_tree(node):
    with open("tree.txt", "w") as write_file:
        write_file.write(RenderTree(node, style=AsciiStyle()).__str__())


def part_one(root):
    return sum(
        node.get_size() for node in PostOrderIter(root) if node.get_size() < 100_000
    )


def part_two(_dir):
    result = float("inf")
    target = _dir.get_size() - 40_000_000
    sizes = [node.get_size() for node in PostOrderIter(root)]
    for size in sizes:
        if size >= target:
            result = min(size, result)
    return result


if __name__ == "__main__":
    root = parse_input()
    write_tree(root)

    print(f"part 1: {part_one(root)}")
    print(f"part 2: {part_two(root)}")
