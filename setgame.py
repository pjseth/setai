import random

class SetGame:
    def __init__(self):
        self.deck = self.make_deck()
        self.game = self.start_game()
        self.match = None
        self.score = 0

    def make_deck(self):
        shapes = ["♦", "~", "⬮"]
        colors = ["R", "G", "P"]
        numbers = [1, 2, 3]
        shadings = ["Solid", "Stripe", "Open"]

        deck = [[s, c, n, sh]
                for s in shapes
                for c in colors
                for n in numbers
                for sh in shadings]

        random.shuffle(deck)
        return deck

    def start_game(self):
        starting_cards = []
        for i in range(12):
            starting_cards.append(self.deck.pop())
        return starting_cards

    def matching(self, card1, card2, card3):
        match = all(
            card1[i] == card2[i] == card3[i] or card1[i] != card2[i] != card3[i] != card1[i]
            for i in range(4)
        )
        return match
    

# Example of using the SetGame class
if __name__ == "__main__":
    set_game = SetGame()
    while(1):
        print("Score: ",set_game.score)
        for card in set_game.game:
            print(set_game.game.index(card)+1, card)
        card1 = set_game.game[int(input("\nSelect Card 1: "))-1]
        print(card1)
        card2 = set_game.game[int(input("\nSelect Card 2: "))-1]
        print(card2)
        card3 = set_game.game[int(input("\nSelect Card 3: "))-1]
        print(card3)
        print("\n")
        set_game.match = set_game.matching(card1, card2, card3)

        if(set_game.match):
            set_game.score +=1
            print("Match! Point+1\n")
            set_game.game.remove(card1)
            set_game.game.remove(card2)
            set_game.game.remove(card3)
            for i in range(3):
                set_game.game.append(set_game.deck.pop())
        else:
            print("No Match! Try Again\n")


    print(set_game.match)