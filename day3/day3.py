priority = 0
threepriority = 0
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
           "A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
three_group = []
count = 0


with open('/Users/eunicekoo/Downloads/PycharmProjects/AOC/day3/input.txt') as f:
    contents = f.read().split("\n")
    for line in contents:
        half = int(len(line)/2)
        first_half = line[:half]
        second_half = line[half:]
        three_group.append(line)
        count += 1

        if count == 3:
            count = count - 3
            for letter in three_group[0]:
                if letter in three_group[1]:
                    if letter in three_group[2]:
                        threepriority += letters.index(letter) + 1
                        three_group.remove(three_group[0])
                        three_group.remove(three_group[0])
                        three_group.remove(three_group[0])
                        break

        for letter in first_half:
            if letter in second_half:
                priority += letters.index(letter) + 1
                break


print(priority)
print(threepriority)
