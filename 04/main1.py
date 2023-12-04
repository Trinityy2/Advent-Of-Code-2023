filename = "input.txt"

total_points = 0
with open(filename) as file:
    for line in file:
        line = line.split(': ')[1]
        win_nums, card_nums = line.split(' | ')
        win_nums = win_nums.split()
        card_nums = card_nums.split()
        num_of_wins = 0
        card_points = 0
        for num in card_nums:
            if num in win_nums: 
                num_of_wins += 1
        if num_of_wins > 0:
            card_points = 2 ** (num_of_wins-1) if num_of_wins > 1 else 1
        total_points += card_points

print(total_points)