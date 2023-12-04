filename = "input.txt"

total_points = 0
current_card = 0

num_of_cards = {}   # recorded as {<card_no>:<no_of_cards>}
with open(filename) as file:
    for line in file:
        current_card += 1
        line = line.split(': ')[1]
        win_nums, card_nums = line.split(' | ')
        win_nums = win_nums.split()
        card_nums = card_nums.split()
        num_of_wins = 0

        # Before we start, also add original to number of cards
        num_of_cards[current_card] = num_of_cards[current_card] + 1 if current_card in num_of_cards.keys() else 1
        for num in card_nums:
            if num in win_nums: 
                num_of_wins += 1
        
        for x in range(current_card + 1, current_card + num_of_wins + 1):
            num_of_cards[x] = num_of_cards[x] + (1 * num_of_cards[current_card]) if x in num_of_cards.keys() else 1 * num_of_cards[current_card]

        print(current_card, num_of_cards)
        

print(sum(num_of_cards.values()))