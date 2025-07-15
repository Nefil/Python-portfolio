import random
import sys

wallet = 400
bet = 200

cards = {
    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

def hand_value(hand):
    # Calculate the value of the hand, converting all aces from 11 to 1 as needed
    values = [cards[card] for card in hand]
    while sum(values) > 21 and values.count(11):
        idx = values.index(11)
        values[idx] = 1
    return sum(values)

def print_hand(label, hand):
    print(f"{label}: {' '.join(hand)} (sum: {hand_value(hand)})")

print(f"Your wallet: {wallet}$")
print(f"You need {bet}$ to start the game")
start = input("Welcome to Black Jack! Do you want to start the game? (yes/no) ").lower().strip()

if start == "yes":
    while wallet >= bet:
        wallet -= bet  # Deduct the bet at the start of each round

        # Draw two cards for the dealer and player
        dealer_cards = [random.choice(list(cards.keys())) for _ in range(2)]
        player_cards = [random.choice(list(cards.keys())) for _ in range(2)]

        print_hand("Dealer's card", [dealer_cards[0]])
        print_hand("Your cards", player_cards)

        # Check for initial blackjack (21 points with two cards)
        player_blackjack = hand_value(player_cards) == 21 and len(player_cards) == 2
        dealer_blackjack = hand_value(dealer_cards) == 21 and len(dealer_cards) == 2

        if player_blackjack or dealer_blackjack:
            print_hand("Dealer's cards", dealer_cards)
            if player_blackjack and dealer_blackjack:
                print("Draw! Both have blackjack! You get your bet back.")
                wallet += bet
            elif player_blackjack:
                print("Blackjack! You win 1.5x bet! (+300$)")
                wallet += int(bet * 2.5)
            else:
                print("Dealer has blackjack! You lose your bet.")
            print(f"Your wallet: {wallet}$")
            end = input("Do you want to exit the game? (yes/no) ").lower().strip()
            if end == "yes":
                break
            continue

        choice = input("Do you want to get another card? (yes/no) ").lower().strip()
        if choice == "yes":
            player_cards.append(random.choice(list(cards.keys())))
            print_hand("Your cards", player_cards)
        else:
            print("You chose not to get another card.")

        # Dealer randomly draws a third card or not (not realistic, but as in the original)
        if random.randint(1, 2) == 1:
            dealer_cards.append(random.choice(list(cards.keys())))
            print("The dealer drew a third card.")
        else:
            print("The dealer didn't draw a third card.")

        print_hand("Dealer's cards", dealer_cards)

        sum_player = hand_value(player_cards)
        sum_dealer = hand_value(dealer_cards)

        # Determine the result of the round
        if sum_player > 21 and sum_dealer > 21:
            print("Draw! Both hands exceed 21! You get your bet back.")
            wallet += bet
        elif sum_dealer > 21:
            print("Dealer busted! You win (+400$)")
            wallet += bet * 2
        elif sum_player > 21:
            print("You busted! You lose your bet.")
        elif sum_player > sum_dealer:
            print("You win! (+400$)")
            wallet += bet * 2
        elif sum_player < sum_dealer:
            print("Dealer wins! You lose your bet.")
        else:
            print("Draw! You get your bet back.")
            wallet += bet

        print(f"Your wallet: {wallet}$")
        if wallet < bet:
            print("You don't have enough money to play again.")
            break

        end = input("Do you want to exit the game? (yes/no) ").lower().strip()
        if end == "yes":
            break
else:
    sys.exit(0)
