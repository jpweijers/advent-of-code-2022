from collections import defaultdict
from itertools import product, combinations


def parse_input(file_name):
    rates = {}
    graph = defaultdict(list)

    with open(file_name) as f:
        for field in map(str.split, f):
            name = field[1]
            flow_rate = int(field[4][5:-1])
            neighbors = list(map(lambda x: x.rstrip(","), field[9:]))

            rates[name] = flow_rate

            for n in neighbors:
                graph[name].append(n)

    return rates, graph


def score(rates, chosen_values):
    return sum(rates[v] * time_left for v, time_left in chosen_values.items())


def floyd_warshall(graph):
    distances = defaultdict(lambda: defaultdict(lambda: float("inf")))

    for a, bs in graph.items():
        distances[a][a] = 0

        for b in bs:
            distances[a][b] = 1
            distances[b][b] = 0

    for a, b, c in product(graph, graph, graph):
        bc, ba, ac = distances[b][c], distances[b][a], distances[a][c]

        if ba + ac < bc:
            distances[b][c] = ba + ac

    return distances


def dfs(distances, rates, valves, time=30, cur="AA", chosen: dict = None):
    if chosen is None:
        chosen = {}

    for nxt in valves:
        new_time = time - (distances[cur][nxt] + 1)
        if new_time < 2:
            continue
        new_chosen = chosen | {nxt: new_time}
        new_valves = valves - {nxt}
        yield from dfs(distances, rates, new_valves, new_time, nxt, new_chosen)

    yield chosen


def part_one():
    rates, graph = parse_input("input.txt")
    distances = floyd_warshall(graph)

    non_zero_valves = set(filter(rates.get, graph.keys()))

    return max(score(rates, c) for c in dfs(distances, rates, non_zero_valves))


def part_two():
    rates, graph = parse_input("input.txt")
    distances = floyd_warshall(graph)

    good = set(filter(rates.get, graph.keys()))

    maxscore = defaultdict(int)

    for solution in dfs(distances, rates, good, 26):
        k = frozenset(solution)
        s = score(rates, solution)
        if s > maxscore[k]:
            maxscore[k] = s

    best = 0
    for (k1, score1), (k2, score2) in combinations(maxscore.items(), 2):
        if len(k1 & k2) != 0:
            continue
        best = max(best, (maxscore[k1] + maxscore[k2]))

    return best


if __name__ == "__main__":
    print(f"Part one: {part_one()}")
    print(f"Part two: {part_two()}")
