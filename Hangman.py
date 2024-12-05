import string 
from IPython.display import clear_output
import random 

print("Hi this is the Hangman game.\nHangman is a game where you have to guess a word, but you have a limited number of attempts to choose letters.\nBut before you start, choose a theme and difficulty")

class Hangman:
    themes = {"Animals": ["lion", "elephant", "dolphin", "giraffe", "kangaroo", "penguin", "zebra", "tiger", "gorilla", "owl", "shark", "fox", "rabbit", "bear", "cat", "turtle", "dog", "hippopotamus"],
               "Food": ["pizza", "sushi", "tacos", "pasta", "salad", "burger", "chocolate", "curry", "bread", "cheese", "chicken", "fish", "apple", "rice", "vegetable", "pancake"],
                "Countries": ["armenia", "canada", "brazil", "uganda", "france", "germany", "italy", "japan", "china", "india", "australia", "russia", "nigeria", "mexico", "spain", "argentina", "netherlands", "sweden", "switzerland"]}
    difficulty = {"Easy": 15, "Medium": 12, "Hard": 9, "Extreme": 5}

    def __init__(self, letters):
        self.letters = list(letters)
        self.progress = []  
        self.word = "" 
        self.attempts = 0
        self.splited_word = []

    def choose_the_theme(self):
        self.themes_list = list(self.themes.keys())
        print("Here are the themes`")
        print(f"1.{self.themes_list[0]} \n2.{self.themes_list[1]} \n3.{self.themes_list[2]}")
        self.theme_choice = int(input("Choose a theme:"))
        
        if self.theme_choice == 1:
            self.word = random.choice(self.themes["Animals"])
        elif self.theme_choice == 2:
            self.word = random.choice(self.themes["Food"])
        elif self.theme_choice == 3:
            self.word = random.choice(self.themes["Countries"])


    def choose_difficulty(self):
        self.difficulties_list = list(self.difficulty.keys())
        print("Here are the Difficulty levels`")
        print(f"1.{self.difficulties_list[0]}\n 2.{self.difficulties_list[1]}\n 3.{self.difficulties_list[2]}\n 4.{self.difficulties_list[3]}")
        self.difficulty_choice = int(input("Choose difficulty level: "))

        if self.difficulty_choice == 1:
            self.attempts = self.difficulty["Easy"]
        elif self.difficulty_choice == 2:
            self.attempts = self.difficulty["Medium"]
        elif self.difficulty_choice == 3:
            self.attempts = self.difficulty["Hard"]
        elif self.difficulty_choice == 4:
            self.attempts = self.difficulty["Extreme"]

    def show_progress(self):
        if not self.progress:
            self.progress = ["_"] * len(self.word)
            self.splited_word = list(self.word)

        print(f"Your progress is: {self.progress}")
        print(f"Letters left: {self.letters}")

    def win_or_lose(self):
        if self.attempts == 0:
            print(f"You lost! The word was: {self.word}")
            return False
        elif self.progress == self.splited_word:
            print("Congratulations! You won!")
            return True
        return None

    def process(self):
        self.letter_choice = input("Choose a letter: ")

        if self.letter_choice in self.word:
            for index, letter in enumerate(self.word):
                if letter == self.letter_choice:
                    self.progress[index] = self.letter_choice
            self.letters.remove(self.letter_choice)
        else:
            if self.letter_choice in self.letters:
                self.letters.remove(self.letter_choice)
                self.attempts -= 1
    
    def replay(self):
        self.rp = input("Do you want to play again?('y' or 'n'): ")

        if self.rp == "y":
            return True
        else:
            return False 

    def game(self):
        while True:
            self.__init__(list(string.ascii_lowercase)) 
            self.choose_the_theme()
            self.choose_difficulty()

            while True:
                print("***")
                self.show_progress()
                self.process()

                result = self.win_or_lose()
                
                if result is not None:
                    break

            if not self.replay():
                break


            

hangman_game = Hangman(list(string.ascii_lowercase))
hangman_game.game()
