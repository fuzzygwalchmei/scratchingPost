import random

words = ['pizza','fairy', 'cactus']

word = random.choice(words)

guesses = []
heart = u'\u2764'
lives = 5

x=0

while lives > 0:
    output = [word[i] if word[i] in guesses else '_' for i in range(len(word))]
    print(output)
    print(f'Lives: {lives * heart}')
    guess = input('pick a letter: ')
    guesses.append(guess)
    if guess not in word:
        lives -= 1
    x +=1


