import random
import sys, os

wallet = 400

cards = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}

print(f"Your wallet: {wallet}$")
print("You need 200$ to start the game")
start = input("Welcome to Black Jack! Do you want to start the game? (yes/no) ").lower().strip()

if start == "yes":
    while wallet >= 200:
        dealer_cards = []
        player_cards = []

        # Dealer draws 2 cards
        for _ in range(2):
            dealer_cards.append(random.choice(list(cards.keys())))
        print("Dealer's card:", dealer_cards[0])

        # Player draws 2 cards
        for _ in range(2):
            player_cards.append(random.choice(list(cards.keys())))
        print("Your cards:", *player_cards)

        # Ask the player if they want another card
        choice = input("Do you want to get another card? (yes/no) ").lower().strip()
        if choice == "yes":
            player_cards.append(random.choice(list(cards.keys())))
            print("Your cards:", *player_cards)
        else:
            print("You chose not to get another card.")

        # Dealer randomly draws a third card or not
        if random.randint(1, 2) == 1:
            dealer_cards.append(random.choice(list(cards.keys())))
            print("The dealer drew a third card.")
        else:
            print("The dealer didn't draw a third card.")

        print("Dealer's cards:", *dealer_cards)

        # Calculate the player's total with Ace adjustment
        player_values = [cards[card] for card in player_cards]
        while sum(player_values) > 21 and "A" in player_cards:
            for i, card in enumerate(player_cards):
                if card == "A" and player_values[i] == 11:
                    player_values[i] = 1
                    break
        sum_player = sum(player_values)

        # Calculate the dealer's total with Ace adjustment
        dealer_values = [cards[card] for card in dealer_cards]
        while sum(dealer_values) > 21 and "A" in dealer_cards:
            for i, card in enumerate(dealer_cards):
                if card == "A" and dealer_values[i] == 11:
                    dealer_values[i] = 1
                    break
        sum_dealer = sum(dealer_values)

        # Determine the game result
        if sum_player > 21 and sum_dealer > 21:
            print("Draw! Both hands exceed 21!")
        elif sum_dealer > 21:
            print("You win! +200$")
            wallet += 200
        elif sum_player > 21:
            print("You lose 200$")
            wallet -= 200
        elif sum_player > sum_dealer:
            print("You win! +200$")
            wallet += 200
        elif sum_player < sum_dealer:
            print("You lose 200$")
            wallet -= 200
        else:
            print("Draw! No wallet change.")

        print(f"Your wallet: {wallet}$")

        end = input("Do you want to exit the game? (yes/no) ").lower().strip()
        if end == "yes":
            wallet = 0
            os.system("cls")

else:
    sys.exit(0)
