first_half = []
second_half = []
total = 0
partial_total = 0

with open('/Users/eunicekoo/Downloads/PycharmProjects/AOC/day4/input.txt') as f:
    contents = f.read().splitlines()
    for line in contents:
        one, two = line.split(",")

        for i in range((int(one.split("-")[0])), (int(one.split("-")[1]) + 1)):
            first_half.append(i)

        for i in range((int(two.split("-")[0])), (int(two.split("-")[1]) + 1)):
            second_half.append(i)

        if set(first_half).issubset(second_half) or set(second_half).issubset(first_half):
            total += 1

        if set(first_half).intersection(second_half):
            partial_total += 1

        first_half.clear()
        second_half.clear()

print(total)
print(partial_total)
