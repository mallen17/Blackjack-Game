# Blackjack

import random

def the_deck():
    deck = []
    vis_deck = []
    for i in range(4):
        for j in range(13):
            deck.append(j+1)
            vis_deck.append(f"[{j+1}]")
    for i in range(len(deck)):
        if deck[i] == 1:
            vis_deck[i] = "[A]"
            deck[i] = 11
        elif deck[i] == 11:
            vis_deck[i] = "[J]"
            deck[i] = 10
        elif deck[i] == 12:
            vis_deck[i] = "[Q]"
            deck[i] = 10
        elif deck[i] == 13:
            vis_deck[i] = "[K]"
            deck[i] = 10
    return deck, vis_deck

def deal_me_up():
    deck, vis_deck = the_deck()
    size = 52
    first_four = []
    vis_cards = []
    for i in range(4):
        index = random.randint(0,size-1-i)
        first_four.append(deck[index])
        del deck[index]
        vis_cards.append(vis_deck[index])
        del vis_deck[index]
    player = [first_four[0], first_four[2]]
    dealer = [first_four[1], first_four[3]]
    return player, dealer, deck, vis_deck, vis_cards

def game():
    # Setup Area
    player, dealer, deck, vis_deck, vis_cards = deal_me_up()
    size = 48
    stand = True
    player_visual = f"Your Cards: \n{vis_cards[0]}{vis_cards[2]}"
    dealer_visual = f"Dealer's Cards: \n[X]{vis_cards[3]}"
    print(dealer_visual)
    print(player_visual)
    # Player Input Area
    while sum(player) < 21 and stand:
        user = int(input("\nDo you HIT or STAND? (1 or 2): "))
        if user == 1:
            index = random.randint(0, size-1)
            player.append(deck[index])
            player_visual += f"{vis_deck[index]}"
            del deck[index]
            del vis_deck[index]
            size -= 1
            print(dealer_visual)
            print(player_visual)
            if 11 in deck and sum(player) > 21:
                for i in range(len(player)):
                    if player[i] == 11:
                        player[i] = 1
        elif user == 2:
            stand = False
    # Dealer Process and Results Area   
    dealer_visual = dealer_visual.replace("[X]", f"{vis_cards[1]}")
    if sum(player) > 21:
        print("WOOOOOAAAAHH!!!! YOU JUST BUSTED BIG TIME")
    elif sum(player) == 21:
        print(dealer_visual)
        print("\nPerfect 21! You Win!")
    else:
        input("Dealer Reveal")
        print()
        print(dealer_visual)
        while sum(dealer) < sum(player) and sum(dealer) < 18:
            input()
            index = random.randint(0, size-1)
            dealer.append(deck[index])
            dealer_visual += f"{vis_deck[index]}"
            del deck[index]
            del vis_deck[index]
            size -= 1
            print(dealer_visual)
            print(player_visual)
            if 11 in deck and sum(dealer) > 21:
                for i in range(len(dealer)):
                    if dealer[i] == 11:
                        dealer[i] = 1
        if sum(dealer) > 21:
            print("Dealer busted so big good win. This is why we gamble.")
        elif sum(dealer) == sum(player):
            print("Apparently this is called a push. Nobody wins.")
        else:
            print("Damn. Should've hit I guess.")
    
def main():
    print("Welcome to Blackjack!\n")
    input("Press Enter to start playing.")
    game()

    
main()
