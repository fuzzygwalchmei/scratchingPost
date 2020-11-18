import random

words = ['pizza','fairy', 'cactus']

word = random.choice(words)

guesses = []
x=0

while x < 5:
    output = [word[i] if word[i] in guesses else '_' for i in range(len(word))]
    print(output)
    guesses.append(input('pick a letter: '))
    
    x +=1

