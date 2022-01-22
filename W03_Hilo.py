import random
from random import randint


class Game:
    def __init__(self):
        self.score = 300
        self.card = 0
        self.guess = 0
        self.hilo = ""
        
        
        
    def card_Value(self):
        self.card_Value = randint(0, 13)
        print(self.card_Value)

    def next(self):
        self.hilo = input("Will the next card be higher or lower?")
        if self.hilo == "higher":
            self.card = randint(0, 13)
            
        elif self.hilo == "lower":
            self.card = randint(0, 13)
    
    def check_guess(self):  
        if self.guess > self.card or self.guess < self.card:
            self.score - 75
            print("Sorry. Try again!")

        elif self.guess == self.card:
            self.score + 100
            print("Good Job you nailed it!")

    def check_score(self):
        if self.score == 0:
            quit()
        
def main():
    g = Game()
       
    answer = ""
    while answer != "n":
        answer = input("Would you like a card? ")
        if answer == "y":
            g.card_Value()
            g.next()
            g.check_guess()
            g.check_score()
            
        elif answer == "n":
            print("Thanks for playing! Have a good day!")   
    
    
    
if __name__ == "__main__":
    main()  