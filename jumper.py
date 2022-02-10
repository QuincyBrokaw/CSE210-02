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
        if self.guesses == self.word:
            print()
            print("Congrats you win!")
            quit()
        else:
            print("nope")
            
class Hangman_graphic:
    def __init__(self):
        pass
    
    if guesses == -1: # you won graphic
        print("      ___     ")        
        print("     /___\    ")
        print("     \   /    ")
        print("      \ /     ")
        print("       0      ")
        print("      /|\     ")
        print("      / \     ")
        print("^^^^^^^^^^^^^^")
        print("You just saved me!")
        print("You won!")
    elif guesses == 0:
        print("      ___        ")
        print("     /___\    ")
        print("     \   /    ")
        print("      \ /     ")
        print("       0      ")
        print("      /|\     ")
        print("      / \     ")
        print("^^^^^^^^^^^^^^")
    elif guesses == 1:
        print("              ")
        print("     /___\    ")
        print("     \   /    ")
        print("      \ /     ")
        print("       0      ")
        print("      /|\     ")
        print("      / \     ")
        print("^^^^^^^^^^^^^^")
    elif guesses == 2:
        print("              ")
        print("              ")
        print("     \   /    ")
        print("      \ /     ")
        print("       0      ")
        print("      /|\     ")
        print("      / \     ")
        print("^^^^^^^^^^^^^^")
    elif guesses == 4:
        print("              ")
        print("              ")
        print("              ")
        print("      \ /     ")
        print("       0      ")
        print("      /|\     ")
        print("      / \     ")
        print("^^^^^^^^^^^^^^")
    elif guesses == 5:
        print("       0      ")
        print("      /|\     ")
        print("      / \     ")
        print("^^^^^^^^^^^^^^")
    else:   # you lost graphic
        print("              ")
        print("              ")
        print("      X       ")
        print("     /|\      ")
        print("     / \      ")
        print("^^^^^^^^^^^^^^")
        print("The noose tightens around your neck, and you feel the")
        print("sudden urge to urinate.")
        print("GAME OVER!")        
            
class Score:
    def __init__(self):
        self.score = 0
        
    def keep_score(self):
        self.score += 1
    
class Chute:
    def __init__(self):
        self.chute_values = ['___','/', '___','\\', '\\', '/', '\\', '/', 'o','/', '|', '\\', '/','\\',]
        # Stores the hangman's body values to be shown to the player
        self.show_chuteman_values = [' ', ' ', ' ', ' ', ' ', ' ', ' ',' ',' ',' ', ' ',' ', ' ',]
        def print_chuteman(values):
            print()
            print("\t   {}".format(values[0]))
            print("\t {}{}{}".format(values[1], values[2], values[3]))
            print("\t {}  {} ".format(values[4], values[5]))
            print("\t {}  {}".format(values[6], values[7], ))
            print("\t   {}    ".format(values[8]))
            print("\t {}{}{}     ".format(values[9],values[10], values[11]))
            print("\t  {}{}       ".format(values[12], values[13]))
            print("               ")
            print("  `````````````````````")
            print()    

class Parachute:
    def __init__(self):
        self.score = 4
    def disp(self):
        if self.score == 4:
            print(" ___ ")
            print("/___\\")
            print("\\   /")
            print(" \\ /")
            print("  0")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
        elif self.score == 3:
            print("/___\\")
            print("\\   /")
            print(" \\ /")
            print("  0")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
        elif self.score == 2:
            print("\\   /")
            print(" \\ /")
            print("  0")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
        elif self.score == 1:
            print(" \\ /")
            print("  0")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
        elif self.score == 0:
            print("  x")
            print(" /|\\")
            print(" / \\")
            print("")
            print("^^^^^^^")
    def score_number(self, number):
        self.score = number
        
def main():
    answer = ""
    g = Guess()
    h = Hangman_graphic()
    s = Score()
    c = Chute()
    p = Parachute()
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
        s.keep_score()
        c.print_chuteman()
        p.disp()
        p.score_number()
        
        
        
        
if __name__ == "__main__":
    main() 