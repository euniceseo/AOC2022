elves = []
calories = 0

with open('/Users/eunicekoo/Downloads/PycharmProjects/AOC/day1/input.txt') as f:
    contents = f.read().splitlines()
    for line in contents:
        if line == '':
            elves.append(calories)
            calories = 0
        else:
            calories = calories + int(line)

topElf = max(elves)
print(topElf)
elves.sort(reverse=True)
print(elves)
print (71124 + 67422 + 66093)

