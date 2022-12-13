def parse_input():
    pairs = []
    with open("input.txt") as f:
        pairs = f.read().split("\n\n")
        pairs = [pair.split("\n") for pair in pairs]
        pairs = [(eval(pair[0]), eval(pair[1])) for pair in pairs]
    return pairs


class Element:
    def __init__(self, val):
        self.val = val

    def __le__(self, other) -> bool:
        if isinstance(self.val, int) and isinstance(other.val, int):
            return self.val <= other.val
        elif isinstance(self.val, int) and isinstance(other.val, list):
            newself = Element([self.val])
            return newself <= other
        elif isinstance(self.val, list) and isinstance(other.val, int):
            newother = Element([other.val])
            return self <= newother
        else:  # both are lists
            for left, right in zip(self.val, other.val):
                l = Element(left)
                r = Element(right)
                if l < r:
                    return True
                elif l > r:
                    return False

            return len(self.val) <= len(other.val)

    def __lt__(self, other) -> bool:
        if isinstance(self.val, int) and isinstance(other.val, int):
            return self.val < other.val
        elif isinstance(self.val, int) and isinstance(other.val, list):
            newself = Element([self.val])
            return newself < other
        elif isinstance(self.val, list) and isinstance(other.val, int):
            newother = Element([other.val])
            return self < newother
        else:
            for left, right in zip(self.val, other.val):
                l = Element(left)
                r = Element(right)
                if l < r:
                    return True
                elif l > r:
                    return False

        return len(self.val) < len(other.val)

    def __gt__(self, other) -> bool:
        if isinstance(self.val, int) and isinstance(other.val, int):
            return self.val > other.val
        elif isinstance(self.val, int) and isinstance(other.val, list):
            newself = Element([self.val])
            return newself > other
        elif isinstance(self.val, list) and isinstance(other.val, int):
            newother = Element([other.val])
            return self > newother
        else:
            for left, right in zip(self.val, other.val):
                l = Element(left)
                r = Element(right)
                if l > r:
                    return True
                elif l < r:
                    return False

        return len(self.val) > len(other.val)


def part_one(pairs):
    result = 0
    for i, pair in enumerate(pairs, start=1):
        left, right = map(Element, pair)
        if left <= right:
            result += i
    return result


if __name__ == "__main__":
    pairs = parse_input()
    print(f"Part one: {part_one(pairs)}")
