# Part 1
digit_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
total = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        int_only = [character for character in line if character in digit_set]
        total += int(f"{int_only[0]}{int_only[-1]}")

print(total)