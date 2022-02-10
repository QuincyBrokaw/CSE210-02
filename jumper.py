import random

class Guess:   #This is where I set the global variables to be changed during game play
    def __init__(self):
        self.list = ["cat", "dog", "cow", "rat"]
        self.letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", 
                        "v", "w", "x", "y", "z"]
        self.guesses = []
        self.word = []
        self.random_list =""
        self.check = ""
        
    def get_word(self):
       self.random_list = random.choice(self.list)
       
    def add_letter_to_dict(self, x):
       self.guesses.append(x)
       
    def add_word(self):
        for i in range(0, len(self.random_list)):
            self.word.append(self.word[i])
            
    def check_guess(self):
        pass
            
            
        
        
def main():
    answer = ""
    g = Guess()
    g.get_word()
    g.add_word()
    while answer != "quit":
        print()
        print(g.random_list)
        print()
        answer = input("Guess a letter [a-z]: ")
        g.add_letter_to_dict(answer)    
        print(g.word)
        print(g.guesses)
        g.check_guess()
        
if __name__ == "__main__":
    main() 