def parse_input(file_name: str) -> str:
    signal = ""
    with open(file_name) as in_file:
        for line in in_file:
            signal += line
    return signal


def find_unique_sequence(signal: str, length: int) -> int:
    for i in range(len(signal[: -length - 1])):
        if len(set(signal[i : i + length])) == length:
            return i + length


if __name__ == "__main__":
    signal = parse_input("input.txt")
    print(f"Part 1: {find_unique_sequence(signal, 4)}")
    print(f"Part 2: {find_unique_sequence(signal, 14)}")
