import time
import requests

KEY = "yourkeyhere"
HEADERS = {"x-rapidapi-key": KEY,
	"x-rapidapi-host": "wordsapiv1.p.rapidapi.com"}

word = requests.get(url="https://wordsapiv1.p.rapidapi.com/words/?random=true", headers=HEADERS).json()['word']

guesses = int(input("How many guesses do you want? (A lot is recommended as theres alot of possible words...): "))
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
