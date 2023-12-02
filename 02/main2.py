filename = "input.txt"

total_power = 0

with open(filename) as f:
    for line in f:
        min_bag = {}
        game_no, game_sets = line.strip().split(": ")
        game_no = int(game_no[5:])
        for game_set in game_sets.split('; '):
            for colours in game_set.split(', '):
                no_of_cubes, colour = colours.split(' ')
                no_of_cubes = int(no_of_cubes)
                # Look for min number of cubes
                if colour in min_bag.keys():
                    if no_of_cubes > min_bag[colour]:
                        min_bag[colour] = no_of_cubes
                else:
                    min_bag[colour] = no_of_cubes
            
        # Multiply together then sum
        bag_power = 1
        for colour in min_bag.keys():
            bag_power *= min_bag[colour]
        total_power += bag_power

print(total_power)