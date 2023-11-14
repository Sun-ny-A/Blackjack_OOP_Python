import random


class BlackJack:

    def __init__(self):
        self.suit = ["clubs", "diamonds", "hearts", "spades"]
        self.deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"A","A","A","A","J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
        self.player_hand = []
        self.dealer_hand = []
        self.player_in = True
        self.dealer_in = True

    def dealing_card(self, hand):
        card = random.choice(self.deck)
        hand.append(card)
        self.deck.remove(card)

    def total_hand(self, hand):
        total = 0 
        face_card = ["J", "Q", "K"]
        ace = 0
        for card in hand:
            if card in range(1,11):
                total += card
            elif card in face_card:
                total +=10
            else:
                total += 11
                ace += 1
        while ace and total >21: #converting ace to 1
            total -= 10
            ace -=1
        return total

    def show_dealer_hand(self):
        if len(self.dealer_hand) == 0:
            return "No cards to show."
        elif len(self.dealer_hand) == 1:
            return self.dealer_hand[0]
        else:
            return self.dealer_hand[0], "second card hidden"
        
    def define_hand(self):
        if self.total_hand(self.dealer_hand) > 21:
            print("BUST! Dealer busts, you win!")
        if self.total_hand(self.dealer_hand) == 21:
            print("BLACKJACK! Dealer wins! Better luck next game!")
        if self.total_hand(self.player_hand) == 21:
            print("BLACKJACK! You win!")
        if self.total_hand(self.player_hand) > 21:
            print("BUST! Dealer wins! Better luck next game!")
        elif 21 - self.total_hand(self.dealer_hand) < 21 - self.total_hand(self.player_hand):
            print(f"Dealer has {self.dealer_hand} and you have {self.player_hand}. \nDealer is closer to 21 without going over so dealer wins! \nBetter luck next game!")
        elif 21 - self.total_hand(self.dealer_hand) > 21 - self.total_hand(self.player_hand):
            print(f"Dealer has {self.dealer_hand} and you have {self.player_hand}. \nYou are closer to 21 without going over so you win!")
        

def driver():
    while True:
        welcome = input("Welcome to the Blackjack table. Are you ready to play? Enter [y]es or [q]uit.")
        if welcome.lower() not in ["y", "yes", "q", "quit"]:
            print("Invalid input. Please enter 'y' or 'yes' to start or 'q' or 'quit' to exit.")
        elif welcome.lower() in ["q", "quit"]:
            print("We'll see you next time!")
            break
        else:
            blackjack = BlackJack()
            while True:  #rounds
                print("Let's play! Dealer is shuffling...")
                random.shuffle(blackjack.deck)
                blackjack.dealing_card(blackjack.player_hand)
                blackjack.dealing_card(blackjack.player_hand)
                blackjack.dealing_card(blackjack.dealer_hand)
                blackjack.dealing_card(blackjack.dealer_hand)
                while True:  #Game
                    print(f'Dealer shows one of two hands: {blackjack.show_dealer_hand()}')
                    print(f'Player shows hand, {blackjack.player_hand}, totaling {blackjack.total_hand(blackjack.player_hand)}')
                    if blackjack.player_in:
                        stay_hit = input("Do you want to [1] stay or do you want to [2] hit? Enter a number.")
                        if stay_hit == '1':
                            blackjack.player_in = False
                            break
                        elif stay_hit not in ["1", "2"]:
                            print("Invalid input. Please enter 1 to stay or 2 to hit.")
                        else:
                            blackjack.dealing_card(blackjack.player_hand)
                            if blackjack.total_hand(blackjack.player_hand) >= 21:
                                break
                    if blackjack.total_hand(blackjack.dealer_hand) > 16:  #Dealer must hit if 16 and under, stand above
                        blackjack.dealer_in = False  #Player won't be asked for another turn, hands are compared
                        print(f'Dealer stands: {blackjack.dealer_hand}')
                    else:
                        blackjack.dealing_card(blackjack.dealer_hand)
                    if not blackjack.player_in and not blackjack.dealer_in:
                        break  #Exit loop
                    if blackjack.total_hand(blackjack.dealer_hand) >= 21:
                        break
                if not blackjack.dealer_in:
                    blackjack.define_hand()
                dealer_total = blackjack.total_hand(blackjack.dealer_hand)
                player_total = blackjack.total_hand(blackjack.player_hand)
                if abs(dealer_total - 21) <= 5 or abs(player_total - 21) <= 5:
                    break
                another_round = input("Do you want to play another round? Enter [y]es or [q]uit")
                if another_round.lower() in ["q", "quit"]:
                    print("We'll see you next time!")
                    break
                elif another_round.lower() not in ["y", "yes"]:
                    print("Invalid input. Please enter [y]es to start another round or [q]uit.")




driver()
        


        
    



