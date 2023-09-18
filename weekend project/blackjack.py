import random

class Card:
    def __init__(self, suit, value, card_value):
         
        # Suit of the card spades, heart, club, diamond
        self.suit = suit
 
        # what appears on the card ace, king, queen, jack, 10, 9, 8, 7, 6, 5, 4, 3, 2
        self.value = value
 
        # the value for the card in blackjack. each number gives their value. jack, queen, king is valued at 10 and ace is 1
        self.card_value = card_value

        # blackjack game with 52 cards
    def blackjack_game(deck):
    
        #dealer and player cards at random
        #can only be given 2 cards
        player_cards = []
        dealer_cards = []
    
        # each player gets 2 cards at random
        while len(player_cards,dealer_cards) < 2:
    
            # cards given to both players are at random
            #once a card is given i will have to add another card for each player giving them two in total
            #after each card is given to them i would remove the card from the deck that way there is no repeats of the same card
            (player_cards, dealer_cards) = random.choice(deck)
            (player_cards, dealer_cards).append(player_cards, dealer_cards)
            deck.remove(player_cards, dealer_cards)
    
            # player and dealer count(score)
            player_count += player_cards.card_value
            dealer_count += dealer_cards.card_value
    
            #In case both the cards self.value are the same ([j,j], [10,10], [k,k]), you can split now having two new hands and 
            # an extra random card per hand increasing your odds of winning more money
            if len(player_cards) == 2:
                if player_cards[0].value = card_value[]  and player_cards[1].value = card_value[]:
                    player_cards[0,1].split(player_cards[0,1])
                    player_score = []
                elif player_cards = new_hands
            if dealer_cards[0].value = card_value[]  and dealer_cards[1].value = card_value[]:
                    dealer_score = []
            
            print(player_cards)
            print(dealer_score)

            #the object is to get 21 or close to is without going over. while making your decision you either have to stay wih what
            #  you have or hit(drawing a new card with teh hopes yu do not bust)
            if player_score == 21:
                print("Blackjack")
                while player_score < 21:
                    decision = input("Hit or Stand")
            
            if dealer_score == 21:
                print("Blackack")
                while dealer_score < 21:
                    decision = input("Hit or Stand")


        
            # make sure to print the player cards and score      
            print(player_cards)
            print(dealer_cards)
            print(player_score)
            print(dealer_score)
        if len(decision) != 1 or (decision.upper() != 'hit' and decision.upper() != 'Stand'):
            print("pick your poison")
 
        # if player decides to Hit
        if decision.upper() == 'hit':
 
            # you are dealt a new card at random
            player_card = random.decision(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
 
            # you now have a new score or count
            player_score += player_card.card_value
      
 
            # print the cards of both players
            print("dealer_cards")
            print(dealer_cards[:-1], True)
            print("dealer_cards"), dealer_score - dealer_cards[-1].card_value
 
            print()
 
            print("player_cards")
            print(player_cards, False)
            print("player_score", player_score)
             
        # If player decides to Stand
        if decision.upper() == 'stand':
            break

        if player_cards[0].value = card_value[]  and player_cards[1].value = card_value[]:
                    player_cards[0,1].split(player_cards[0,1])
                    player_score = []

        elif len(decision) != 1 or (decision.upper() != 'hit' and decision.upper() != 'Stand'):
            print("pick your poison")
 
        # if player decides to Hit
        if decision.upper() == 'hit':
 
            # you are dealt a new card at random
            player_card = random.decision(deck)
            player_cards.append(player_card)
            deck.remove(player_card)
 
            # you now have a new score or count
            player_score += player_card.card_value
 
 
    # print player and dealer cards
    print("PLAYER CARDS")
    'print_cards'('player_cards', False)
    print('PLAYER SCORE=', 'player_score')
 
    print()
    print("dealer shows cards")
 
    print("DEALER CARDS: ")
    'print_cards'('dealer_cards', False)
    print("DEALER SCORE = ", 'dealer_score')
 
    # Check if player has a Blackjack
    if 'player_score' == 21:
        print("Player has Blackjack")
        quit()
 
    # Check if player busts
    if 'player_score' > 21:
        print("player bust. Game over")
        quit()
 
    input() 
 
    # Managing the dealer moves
    while 'dealer_score' < 17:
 
 
        print("dealer decision to hit")
 
        # Dealing card for dealer
        dealer_card = random.choice(deck)
        dealer_cards.append(dealer_card)
        deck.remove(dealer_card)
 
        # Updating the dealer's score
        dealer_score += dealer_card.card_value
 
        # Updating player score in case player's card have ace in them
        c = 0
        while dealer_score > 21 and c < len(dealer_cards):
            if dealer_cards[c].card_value == 11:
                dealer_cards[c].card_value = 1
                dealer_score -= 10
                c += 1
            else:
                c += 1
 
        # print player and dealer cards
        print("player cards: ")
        'print_cards'('player_cards', False)
        print("player score = ", 'player_score')
 
        print()
 
        print("dealer cards: ")
        'print_cards'('dealer_cards', False)
        print("dealer score = ", 'dealer_score')      
 
        input()
 
    # if the dealer busts
    if 'dealer_score' > 21:        
        print("dealer bust . you win") 
        quit()  
 
    # if the dealer shows blackjack on first first cards.
    if 'dealer_score' == 21:
        print("dealer had blackjack. player loses")
        quit()
 
    # if the game ends in a tie
    if 'dealer_score' == 'player_score':
        print("TIE GAME!!!!")
 
    # Player Wins
    elif 'player_score' > 'dealer_score':
        print("player wins")                 
 
    # Dealer Wins
    else:
        print("dealer wins")                 
 
if __name__ == '__main__':
 
    # The type of suit
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
 
    # The type of card
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
 
    # The card value
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
 
    # The deck of cards
    deck = []
 
    # Loop for every type of suit
    for suit in suits:
 
        # Loop for every type of card in a suit
        for card in cards:
 
            # Adding card to the deck
            deck.append(Card(cards_values[suit], card, cards_values[card]))
     
    card(deck)

