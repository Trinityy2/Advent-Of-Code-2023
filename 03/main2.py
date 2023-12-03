filename = "input.txt"

schematic = []
with open(filename) as file:
    for line in file:
        schematic.append(line.strip())

asterisk_parts = {}
total_sum = 0

def check_until_period(substring: str, reverse: bool = False) -> int:
        if reverse: substring = substring[::-1]

        # Return the number of positions until its not a number (from left to right)
        pos = 0
        for character in substring:
            if not character.isdigit():
                return pos
            else:
                pos += 1
        return pos

def get_engine_part_details(rows: list, ystart, yend, xstart: int, xend: int) -> list:
    found_gears = []
    for y in range(ystart, yend):
        for x in range(xstart, xend):
            if rows[y][x] != '.' and not rows[y][x].isdigit():
                if rows[y][x] == '*':
                    found_gears.append(f'{y},{x}')
    return found_gears

y = 0
while y < len(schematic):
    x = 0
    while x < len(schematic[y]):
        if schematic[y][x].isdigit():
            # Look for the full number (and the positions we have to check)
            x_start = x - check_until_period(schematic[y][0:x], True)
            x_end = x + check_until_period(schematic[y][x:])
            part_num = int(schematic[y][x_start:x_end])

            # Now use this info to look around for symbol
            x_checker_left = x_start - 1 if x_start != 0 else 0
            x_checker_right = x_end +1 if x_end != len(schematic) else len(schematic)
            y_checker_top = y - 1 if y != 0 else 0
            y_checker_bottom = y + 2 if not((y + 2) > len(schematic)) else len(schematic)

            # if check_for_engine_part(schematic[y_checker_top:y_checker_bottom], x_checker_left, x_checker_right):
            #     total_sum += part_num
            results = get_engine_part_details(schematic, y_checker_top, y_checker_bottom, x_checker_left, x_checker_right)
            if len(results):
                for result in results:
                    if result not in asterisk_parts.keys():
                        asterisk_parts[result] = [part_num]
                    else:
                        asterisk_parts[result].append(part_num)

            x += x_end - x_start
        else:
            x += 1
    y += 1

for k, v in asterisk_parts.items():
    if len(v) == 2:
        total_sum += (v[0]*v[1])

print(total_sum)