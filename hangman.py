import os
import random
import time

from colorama import Fore, init

init(autoreset=True)

class Hangman():
    def __init__(self) -> None:
        self. random_words = [
            "apple", "banana", "orange", "grape", "kiwi", "melon", "strawberry", "pineapple", "peach", "plum",
            "blueberry", "raspberry", "mango", "pear", "cherry", "watermelon", "lemon", "lime", "apricot", "avocado",
            "blackberry", "cantaloupe", "cranberry", "date", "fig", "guava", "honeydew", "kiwifruit", "lychee", "nectarine",
            "papaya", "passionfruit", "pomegranate", "quince", "raisin", "tangerine", "uva", "zucchini", "almond", "cashew",
            "walnut", "pecan", "pistachio", "hazelnut", "macadamia", "peanut", "coconut", "chestnut", "cocoa", "coffee",
            "espresso", "latte", "cappuccino", "mocha", "frappe", "americano", "bagel", "croissant", "muffin", "pancake",
            "waffle", "frenchtoast", "cereal", "oatmeal", "granola", "yogurt", "cheese", "butter", "cream", "milk", "egg",
            "bacon", "sausage", "ham", "panini", "sandwich", "burger", "hotdog", "pizza", "pasta", "lasagna", "sushi",
            "sashimi", "tempura", "ramen", "dumpling", "noodle", "rice", "curry", "soup", "salad", "smoothie", "juice",
            "lemonade", "soda", "water", "tea", "chai", "matcha", "herbal", "ginger", "mint", "rosemary", "thyme", "basil",
            "cinnamon", "vanilla", "chocolate", "caramel", "honey", "maple", "syrup", "jam", "jelly", "preserves", "pickle",
            "relish", "ketchup", "mustard", "mayonnaise", "vinegar", "oil", "garlic", "onion", "pepper", "salt", "sugar",
            "flour", "baking", "cooking", "grilling", "roasting", "steaming", "sauteing", "frying", "baking", "boiling",
            "mixing", "whisking", "chopping", "slicing", "dicing", "peeling", "grating", "measuring", "tasting", "serving"
        ]


        self.letters_used = []
        self.attempts = 0
        self.max_attempts = 5

        self.word = random.choice(self.random_words)

    def display_word(self) -> str:
        return ' '.join(letter if letter in self.letters_used else '_' for letter in self.word)

    def display_incorrect_guesses(self) -> str:
        return ', '.join(letter for letter in self.letters_used if letter not in self.word)

    def game_status(self) -> str:
        return f'''
© anekobtw, 2023
----------------------------------
Attempts: {self.attempts}/{self.max_attempts}
Incorrect guesses: {Fore.RED}{self.display_incorrect_guesses()}
{Fore.RESET}Word: {Fore.GREEN}{self.display_word()}'''

def main():
    hangman = Hangman()
    while True:
        print(hangman.game_status())
        
        if hangman.display_word() == hangman.word:
            print(f'{Fore.GREEN}Congratulations! You won the game!')
            time.sleep(1)
            break
            
        user_input = input('Enter a letter or the word itself: ').lower()

        if user_input == hangman.word:
            print(f'{Fore.GREEN}Congratulations! You won the game!')
            time.sleep(1)
            break
        elif len(user_input) == 1 and user_input.isalpha():
            if user_input in hangman.letters_used:
                print(f'{Fore.LIGHTBLUE_EX}You already guessed that letter. Try again.')
                time.sleep(1)
            else:
                hangman.letters_used.append(user_input)
        else:
            print(f'{Fore.RED}Invalid input. Please enter a single letter or the word itself.')
            time.sleep(1)
            continue
        
        if user_input not in hangman.word:
            hangman.attempts += 1

            if hangman.attempts > hangman.max_attempts:
                print(f'{Fore.RED}You lost the game. The word was:', hangman.word)
                time.sleep(1)
                break

        os.system('clear')

if __name__ == "__main__":
    main()
