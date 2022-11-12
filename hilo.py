"""
hilo game coded by Marina Kreibring
for BYU-I cse210 fall 2022
"""
# import random module to choose cards
import random

"""Class Card represents the card deck.
The function is to draw first card (value) and next card (next_value) and compare them.
"""
class Card:
    def __init__(self):
        self.value = None
        self.next_value = None

    def draw(self):
        # random choice the values of the cards between 1 and 13
        self.value = random.randint(1, 13)
        self.next_value = random.randint(1, 13)

    def is_higher(self):
        # check if the second card is higher, return: true
        return self.next_value >= self.value

    def is_lower(self):
        # check if the second card is lower, return: true
        return self.next_value < self.value



"""Class Director represents the host of the game"""
class Director:
    def __init__(self):
        # starting score is 300
        self.score = 300
        self.card = Card()

    # play the game while user unswers Yes or has score >0
    def play(self):
        want_to_play = "y"
        while want_to_play.lower() == "y" or want_to_play == "":
            self.do_turn()
            print(f"Your score is: {self.score}")

            if self.score <= 0:
                print("Game over!")
                break

            want_to_play = input("Play again? [Y/N] ").strip()
            print()
            print("Thank you for the game!")

    # draw cards and check the results
    def do_turn(self):
        self.card.draw()
        print(f"The card is: {self.card.value}")
        # ask the user for his guess in separate method
        guessed_higher = self.ask_higher()
        print(f"The next card was: {self.card.next_value}")

        if (guessed_higher and self.card.is_higher()) or ((not guessed_higher) and self.card.is_lower()):
            self.score +=100
        else:
            self.score -=75 

    def ask_higher(self):
        # return: True if the user thinks the next card is higher, False if it is lower
        return input("Higher or lower? [h/l] ").lower() == "h"


def main():
    Director().play()


if __name__ == "__main__":
    main()
