import re


class Valve:
    def __init__(self, name, flow_rate):
        self.name = name
        self.flow_rate = flow_rate
        self.neighbors = []

    def __repr__(self):
        return f"{self.name} ({self.flow_rate}) -> {self.neighbors}"


def parse_input(filename="test_input.txt"):
    valves = {}
    with open(filename) as f:
        for line in f:
            name, flow_rate, neighbours = re.findall(
                r"Valve\s([A-Z]{2}).*?rate=(\d+).*?valves*\s(.*)",
                line.strip(),
            )[0]
            valve = Valve(name, int(flow_rate))
            valves[valve.name] = valve
            for neighbour in neighbours.split(", "):
                valve.neighbors.append(neighbour)
           

    return valves

def part_one():
    valves = parse_input()
    position = valves["AA"]
    total_flow = 0
    flow_per_minute = 0

    for _ in range(30, 0, -1):
        print(f"pos: {position.name}, flow: {flow_per_minute}, total: {total_flow}")
        input(valves)
        if position.flow_rate > 0:
            flow_per_minute += position.flow_rate
            position.flow_rate = 0

        # now move
        else:
            _next = valves[position.neighbors[0]]
            if len(position.neighbors) > 1:
                for neighbour in position.neighbors:
                    neighbour = valves[neighbour]
                    if neighbour.flow_rate > _next.flow_rate:
                        _next = neighbour
                

            position = _next

        total_flow += flow_per_minute

    return total_flow


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
