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
        your_cards = {}
        dealercards = {}

        # Dealer's cards
        fcard = random.choice(list(cards.keys()))
        tcard = random.choice(list(cards.keys()))
        dealercards[fcard] = cards[fcard]
        dealercards[tcard] = cards[tcard]
        print("Dealer's card:", fcard)

        # Player's cards
        pkarta = random.choice(list(cards.keys()))
        dkarta = random.choice(list(cards.keys()))
        your_cards[pkarta] = cards[pkarta]
        your_cards[dkarta] = cards[dkarta]
        print("Your cards:", pkarta, dkarta)

        # Asking if the player wants another card
        choice = input("Do you want to get another card? (yes/no) ").lower().strip()
        if choice == "yes":
            tkarta = random.choice(list(cards.keys()))
            your_cards[tkarta] = cards[tkarta]
        else:
            tkarta = ""

        print("Your cards:", list(your_cards.keys()))

        # Dealer randomly draws a third card
        thcard = ""
        if random.randint(1, 2) == 1:
            thcard = random.choice(list(cards.keys()))
            dealercards[thcard] = cards[thcard]
            print("The dealer drew a third card.")
        else:
            print("The dealer didn't draw a third card.")

        print("Dealer's cards:", list(dealercards.keys()))

        # Adjust Aces if over 21
        def adjust_aces(cards_dict):
            while sum(cards_dict.values()) > 21 and "A" in cards_dict:
                for key in list(cards_dict.keys()):
                    if key == "A" and cards_dict[key] == 11:
                        cards_dict[key] = 1
                        break

        adjust_aces(your_cards)
        adjust_aces(dealercards)

        sumycard = sum(your_cards.values())
        sumdcard = sum(dealercards.values())

        def douwant():
            global wallet
            end = input("Do you want to exit the game? (yes/no) ").lower().strip()
            if end == "yes":
                wallet = 0
                os.system("cls")


        if sumycard > 21 and sumdcard > 21:
            print("Draw! Both hands exceed 21!")
        elif sumdcard > 21:
            print("You win! +200$")
            wallet += 200
        elif sumycard > 21:
            print("You lose 200$")
            wallet -= 200
        elif sumycard > sumdcard:
            print("You win! +200$")
            wallet += 200
        elif sumycard < sumdcard:
            print("You lose 200$")
            wallet -= 200
        else:
            print("Draw! No wallet change.")

        print(f"Your wallet: {wallet}$")
        douwant()

else:
    sys.exit(0)