filename = "input.txt"
bag = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

total_sum = 0

with open(filename) as f:
    for line in f:
        game_no, game_sets = line.strip().split(": ")
        game_no = int(game_no[5:])
        for game_set in game_sets.split('; '):
            legal_game = True
            for colours in game_set.split(', '):
                no_of_cubes, colour = colours.split(' ')
                if int(no_of_cubes) > bag[colour]:
                    legal_game = False
                    break
            if not legal_game:
                break
        if legal_game:
            total_sum += game_no

print(total_sum)