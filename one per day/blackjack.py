from random import *
#deal cards to player
#generate 5 different cards and store them in deck
def card_dealer(card_bundle):
    nums = 5
    deck = []
    for i in range(nums):
        x = randrange(0, len(card_bundle))
        if x not in deck:
            deck.append(card_bundle[x])
        else:
            nums = 5 - len(deck)
    return deck


def main():
    suits = ['D','S','C','H']
    nums = ['2','3','4','5','6','7','8','9','J','Q','K','A']
    card_bundle = []
    for i in range(len(suits)):
        # print(suits[i])
        for j in range(len(nums)):
            # print(nums[j])
            # print(str(suits[i] + nums[j]))
            card_bundle.append(str(suits[i] + nums[j]))
    # print(card_bundle)
    deck = card_dealer(card_bundle)
    # print(deck)
    dealer_card = [deck[1], deck[3]]
    player_card = [deck[0], deck[2]]
    player_value = 4 + nums.index((player_card[0][1])) + nums.index((player_card[1][1]))
    if (player_value > 21) and (player_card[0][1] == 'A' or player_card[1][1] == 'A'):
        player_value -= 12
    print(f"Player cards are: {player_card[0]}, {player_card[1]}, and the Value is {player_value}")

    dealer_value = 2 + nums.index(dealer_card[0][1])
    print(f"Dealer cards are: {dealer_card[0]}, and the Value is {dealer_value}")
    # print(f"Player cards are: {player_card[0]}, {player_card[1]}, and the Value is {player_value}")
    # print(f"Dealer cards are: {dealer_card[0]}, {dealer_card[1]}, and the Value is {dealer_value}")
    x = input("Do you want next card (y or n): ")
    if x == "y":
        player_card.append(deck[4])
        player_value = 6 + nums.index((player_card[0][1])) + nums.index((player_card[1][1]))  + nums.index((player_card[2][1]))
        if (player_value > 21) and (player_card[0][1] == 'A' or player_card[1][1] == 'A' or player_card[2][1] == 'A'):
            player_value -= 12
        print(f"Player cards are: {player_card[0]}, {player_card[1]}, {player_card[2]} and the Value is {player_value}")
        dealer_value = 4 + nums.index(dealer_card[0][1]) + nums.index(dealer_card[1][1])
        if (dealer_value > 21) and (dealer_card[0][1] == 'A' or dealer_card[1][1] == 'A'):
            dealer_value -= 12
        print(f"Dealer cards are: {dealer_card[0]}, {dealer_card[1]}, and the Value is {dealer_value}")
        dumm_p = 21 - player_value
        dumm_d = 21 - dealer_value
        if player_value == 21:
            print("Player wins the game")
        elif player_value > 21:
            print("Dealer wins")
        elif player_value < 21 and dumm_p < dumm_d:
            print("Player wins")
        elif player_value < 21 and dumm_p > dumm_d:
            print("Dealer wins")

    else:
        # dealer_card.append(deck[4])
        dealer_value = 4 + nums.index(dealer_card[0][1]) + nums.index(dealer_card[1][1])
        player_value = 4 + nums.index((player_card[0][1])) + nums.index((player_card[1][1]))
        if (player_value > 21) and (player_card[0][1] == 'A' or player_card[1][1] == 'A'):
            player_value -= 12
        print(f"Player cards are: {player_card[0]}, {player_card[1]}, and the Value is {player_value}")
        dealer_value = 4 + nums.index(dealer_card[0][1]) + nums.index(dealer_card[1][1])
        if (dealer_value > 21) and (dealer_card[0][1] == 'A' or dealer_card[1][1] == 'A'):
            dealer_value -= 12
        print(f"Dealer cards are: {dealer_card[0]}, {dealer_card[1]}, and the Value is {dealer_value}")
        dumm_p = 21 - player_value
        dumm_d = 21 - dealer_value
        if player_value == 21:
            print("Player wins the game")
        elif player_value > 21:
            print("Dealer wins")
        elif player_value < 21 and dumm_p < dumm_d:
            print("Player wins")
        elif player_value < 21 and dumm_p > dumm_d:
            print("Dealer wins")
        



if __name__ == "__main__":
    main()
