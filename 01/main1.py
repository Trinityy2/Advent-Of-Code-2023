# Part 1
total = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        int_only = [character for character in line if character.isdigit()]
        total += int(f"{int_only[0]}{int_only[-1]}")

print(total)