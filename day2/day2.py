# Opponent:
# Rock = A (1)
# Paper = B (2)
# Scissors = C (3)

# 6 if win, 3 if draw, 0 if lose

# You:
# Need to lose = X
# Need to draw = Y
# Need to win = Z

score = 0
twoscore = 0;

with open('/Users/eunicekoo/Downloads/PycharmProjects/AOC/day2/input.txt') as f:
    contents = f.read().splitlines()
    for line in contents:
        split = line.split()
        # rock
        if split[0] == 'A':
            if split[1] == 'X':
                # need to lose = play scissors
                score += 1 + 3
                twoscore += 0 + 3
            if split[1] == 'Y':
                # need to draw = play rock
                score += 2 + 6
                twoscore += 3 + 1
            if split[1] == 'Z':
                # need to win = play paper
                score += 3 + 0
                twoscore += 6 + 2
        # paper
        if split[0] == 'B':
            if split[1] == 'X':
                score += 1 + 0
                twoscore += 0 + 1
            if split[1] == 'Y':
                score += 2 + 3
                twoscore += 3 + 2
            if split[1] == 'Z':
                score += 3 + 6
                twoscore += 6 + 3
        # scissors
        if split[0] == 'C':
            if split[1] == 'X':
                score += 1 + 6
                twoscore += 0 + 2
            if split[1] == 'Y':
                score += 2 + 0
                twoscore += 3 + 3
            if split[1] == 'Z':
                score += 3 + 3
                twoscore += 6 + 1

print(score)
print(twoscore)


def parse(inp):
    strat = []
    for line in inp.splitlines():
        a, b = line.split()
        a = ord(a) - ord('A')
        b = ord(b) - ord('X')
        strat.append((a,b))
    return strat

def part1(strat):
    score = 0

    for a, b in strat:
        score += b+1
        score += ((b+1 - a) % 3) * 3
    return score


def part2(strat):
    score = 0

    for a, b in strat:
        score += b*3
        score += ((a+b+2) % 3) + 1
    return score