import deck
import random
import functools
import sys


class Movements():
    def __init__(self):
        super().__init__()

    def set_hand(self, cards):
        self.hand = [*self.hand, *cards]

    def get_points(self):
        if len(self.hand) > 0:
            return functools.reduce(lambda sum, y: sum + int(y.value), self.hand, 0)

    def clear_hand(self):
        self.hand = []

    def get_hand(self, hide=-1):
        if hide >= 0:
            return [f"{x[1].rank} of {x[1].suit} : {x[1].value}" if x[0] != hide else f"* * *" for x in enumerate(self.hand)]
        else:
            return [f"{x.rank} of {x.suit} : {x.value}" for x in self.hand]


class Player(Movements):

    hand = []

    def __init__(self, name="anonymous", balance=100):
        super().__init__()
        Movements()
        self.balance = balance
        self.name = name

    def __str__(self):
        print(f"The player {self.name} have {self.balance}")

    def add(self, qty):
        if qty < 1:
            pass
        else:
            self.balance += qty

    def withdraw(self, qty):
        if qty > self.balance:
            pass
        else:
            self.balance -= qty


class Dealer(Movements):
    hand = []

    def __init__(self):
        Movements()
        super().__init__()


def make_deck(n):
    print(n[0])
    val = [{"suit": n[1], "value":deck.values.get(
        x), "rank":x} for x in deck.ranks]
    return val


class Card():
    def __init__(self, suit, rank, value):
        super().__init__()
        self.suit = suit
        self.rank = rank
        self.value = value

    def __str__(self):
        return f"{self.rank} of {self.suit}: {self.value}"


class Deck():
    def __init__(self):
        super().__init__()
        cards = [x for x in list(map(make_deck, enumerate(deck.suits)))]
        self.base = [Card(rank=x["rank"], value=x["value"], suit=x["suit"])
                     for card in cards for x in card]
        self.cards = self.base

    def new_deck(self):
        self.cards = self.base

    def __str__(self):
        print(self)
        return self.cards

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def giveCards(self, qty):
        values = []
        if len(self.cards) > 0:
            for target_list in range(qty):
                index = random.randint(0, len(self.cards))
                values += [self.cards[index]]
                del self.cards[index]

            return values


class Game():
    max = 21

    def __init__(self, player, dealer):
        super().__init__()
        self.player = player
        self.dealer = dealer

    def give_hand(self, deck):
        self.player.set_hand(deck.giveCards(2))
        self.dealer.set_hand(deck.giveCards(2))

    def set_bet(self):
        while True:
            try:
                bet = int(input("Plase enter the bet quantity: "))
                if bet <= self.player.balance:
                    self.bet = bet
                    break
                else:
                    print(f"please set a bet lower than {self.player.balance}")
            except TypeError as identifier:
                print(f"Some error occurred {identifier}")
            except:
                print("Some error occurred")

    def check_winner(self):
        dealer_points = self.dealer.get_points()
        player_points = self.player.get_points()

        print("------------------------------")
        print(f"YOUR POINTS {player_points}")
        print("------------------------------")
        print(f"DEALER POINTS {dealer_points}")
        print("------------------------------")
        self.player.clear_hand()
        self.dealer.clear_hand()

        if dealer_points == player_points:
            print("--- DRAW ---")
        elif dealer_points <= self.max or player_points - self.max > 0:
            if dealer_points > player_points or player_points > self.max:
                print("--- DEALER WINS ---")
                self.player.withdraw(self.bet)
        elif player_points <= self.max or dealer_points - self.max > 0:
            if player_points > dealer_points or dealer_points > self.max:
                print("--- PLAYER WINS ---")
                self.player.add(self.bet)
        else:
            print("--- DRAW ---")

    def give_card(self, deck, player):
        card = deck.giveCards(1)
        print(
            f"The card is >>> {card[0].rank} of {card[0].suit} : {card[0].value}")
        player.set_hand(card)

    def give_card_dealer(self, deck, dealer):
        card = deck.giveCards(1)
        print(
            f"The card is >>> {card[0].rank} of {card[0].suit} : {card[0].value}")
        dealer.set_hand(card)

    def can_continue(self, player):
        points = player.get_points()
        if points > self.max:
            return False
        else:
            return True

    def continue_ask(self):
        while True:
            ans = input("Do you want another card ? (Y/N): ")
            print(ans)
            if ans == "exit":
                sys.exit()
            elif ans.lower() != "y" and ans.lower() != "n":
                print("----- Please pick a valid option (Y/N) -----")
            elif ans.lower() == "y":
                return True
                break
            elif ans.lower() == "n":
                return False
                break

    def continue_playing(self):
        while True:
            ans = input("Do you want to play another game ? (Y/N): ")
            print(ans)
            if ans == "exit":
                sys.exit()
            elif ans.lower() != "y" and ans.lower() != "n":
                print("----- Please pick a valid option (Y/N) -----")
            elif ans.lower() == "y":
                return True
                break
            elif ans.lower() == "n":
                return False
                break


def play(player, dealer, deck):
    playing = True
    while playing:
        print(f"Welcome {player.name} to the Blackjack game")

        game = Game(player, dealer)
        print("Distributing cards ")
        game.give_hand(deck)
        print(f"Your balance is ${player.balance}")
        game.set_bet()
        deck.new_deck()
        deck.shuffle_deck()
        # game.give_card(deck)

        player_play = True
        dealer_play = True

        while player_play or dealer_play:
            try:

                print("-----------------------------------------")
                print("Your hand is ")
                print(player.get_hand())
                print(f"Your total points: {player.get_points()}")
                print("-----------------------------------------")

                print("The dealer hand is ")
                print(dealer.get_hand(0))
                if player_play:
                    if game.continue_ask() == True and player.get_points() < 21:
                        game.give_card(deck, game.player)
                        print("-----------------------------------------")
                    else:
                        player_play = False

                if dealer_play == True:
                    if dealer.get_points() < 17:
                        game.give_card(deck, game.dealer)
                        print("-----------------------------------------")
                    else:
                        dealer_play = False

            except:
                print("some error happened")
            else:
                if game.can_continue(game.player):
                    print("can continue")
                else:
                    print("You can't continue you reach the limit")
                    player_play = False
        game.check_winner()
        print(f"Your balance is ${player.balance}")
        if player.balance <= 0:
            print("You need money yo play!!!!")
            playing = False

        if game.continue_playing() == False and player.balance > 0:
            playing = False


player = Player("Eduardo", 100)
dealer = Dealer()
deck = Deck()

play(player=player, dealer=dealer, deck=deck)
