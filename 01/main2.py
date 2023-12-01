# Part 2
digit_set = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9',
    "zero": '0'
}
total = 0

with open("input.txt") as file:
    for line in file:
        line = line.strip()
        for k, v in digit_set.items():
            # Numbers in words can share letters (first and last). Try to maintain these
            replace_with = k[0:len(k)//2] + v + k[len(k)//2:]
            line = line.replace(k, replace_with)
        int_only = [character for character in line if character in digit_set.values()]
        total += int(f"{int_only[0]}{int_only[-1]}")

print(total)