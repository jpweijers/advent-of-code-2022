# A rock, B = Paper, C = Scissors
# X = rock, Y = Paper, Z = Scissors
A, B, C = 1, 2, 3
BEATS = {A: C, B: A, C: B}
LOSES = {v:k for k, v in BEATS.items()}

def part_one():
    score = 0
    with open("input.txt") as infile:
        for line in infile:
            elf = ord(line.split()[0]) - 64
            you = ord(line.split()[1]) - 87
            if you == elf:
                score += 3
                score += you
            elif BEATS[you] == elf:
                score += you
                score += 6
            else:
                score += you

        print(score)

def part_two():
    score = 0
    with open("input.txt") as infile:
        # X = lose, Y = draw, Z = win
        for line in infile:
            elf = ord(line.split()[0]) - 64
            you = line.split()[1]
            if "X" in you:
                pick = BEATS[elf]
                score += 0 + pick
            elif "Y" in you:
                pick = elf
                score += 3 + pick
            else:
                pick = LOSES[elf]
                score += 6 + pick

        print(score)
            
if __name__ == "__main__":
    part_one()
    part_two()