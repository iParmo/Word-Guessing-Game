import time
import random

wordList = ["cheese", "cum", "monkey", "food", "drink", "water", "tiger", "chips", "cola", "soda",
            "chicken", "finger", "arm", "head", "penis", "dick", "cock", "rooster", "cocaine",
            "coke", "python", "danish", "british", "american", "turkey", "harry", "potter",
            "harry potter", "ginger", "chili", "meme"]
word = random.choice(wordList)

guesses = int(input("How many guesses do you want?: "))
seconds = 4
print(f'Starting game with {guesses} guesses in...')

for i in range(3):
    seconds -= 1
    print(f'{seconds}', end='\r')
    time.sleep(1)

print("GO!")
guess = ""

while not guess == word:
    guesses -= 1
    guess = input(str("Enter your guess: "))
    print(f'Guesses left: {guesses}')
    if guess == word:
        print(f'You won with {guesses} guesses remaining!')
        break
    elif guesses <= 0:
        print("You lost :(")
        break
