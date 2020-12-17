import time
import requests

KEY = "yourkeyhere"
HEADERS = {"x-rapidapi-key": KEY,
	"x-rapidapi-host": "wordsapiv1.p.rapidapi.com"}

word = requests.get(url="https://wordsapiv1.p.rapidapi.com/words/?random=true", headers=HEADERS).json()['word']
hintCount = -1

guesses = int(input("How many guesses do you want?: "))
seconds = 4
lengthEnd = 0

print(f'Starting game with {guesses} guesses in...')

for i in range(3):
    seconds -= 1
    print(f'{seconds}', end='\r')
    time.sleep(1)

print("GO!")
guess = ""

while not guess == word:
    guesses -= 1
    hintCount += 1
    lengthEnd += 1
    print(f'Your word is {len(word)} characters long.')
    if hintCount == 0:
        print(f'Hint: your words first letter is "{word[0]}"')
    elif hintCount > 0:
        print(f'Hint: {word[:hintCount]}')
    guess = input(str("Enter your guess: "))
    print(f'Guesses left: {guesses}')
    if guess == word:
        print(f'You won with {guesses} guesses remaining!')
        break
    elif guesses <= 0:
        print("You lost :(")
        break
    elif lengthEnd >= len(word):
        print("You lost by guessing more than the word is long!")
        break
