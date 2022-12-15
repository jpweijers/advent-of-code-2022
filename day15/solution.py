import re
from dataclasses import dataclass


@dataclass
class Beacon:
    x: int
    y: int


@dataclass
class Sensor:
    x: int
    y: int
    beacon: Beacon


def parse_input():
    sensors = []
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            sx, sy, bx, by = map(int, re.findall(r"-*\d+", line))
            beacon = Beacon(bx, by)
            sensor = Sensor(sx, sy, beacon)
            sensors.append(sensor)

    return sensors


def part_one(sensors):
    # positions without beacon in row y=2000
    # (total cols) - (beacons in row y=2000000)

    lx = float("inf")
    hx = float("-inf")
    known = set()

    for sensor in sensors:
        distance = abs(sensor.x - sensor.beacon.x) + abs(sensor.y - sensor.beacon.y)
        offset = distance - abs(sensor.y - 2_000_000)

        lx = min(lx, sensor.x - offset)
        hx = max(hx, sensor.x + offset)

        if sensor.beacon.y == 2_000_000:
            known.add(sensor.beacon.x)

    return hx - lx + 1 - len(known)


def part_two(sensors):
    pass


if __name__ == "__main__":
    sensors = parse_input()
    print(f"Part one: {part_one(sensors)}")
    print(f"Part two: {part_two(sensors)}")
