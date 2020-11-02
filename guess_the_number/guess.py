from random import randint

num = randint(1, 101)
guess = 0
guesses = 0

while guess != num:
    guess = int(input(f"Please guess a number between 1 and 100 (guess {guesses}): "))
    guesses += 1
    if guess not in range(1,101):
        print("That number was outside of the range, its only between 1 and 100\n")
    elif guess == num:
        if guesses == 1:
            print("Wow, you guessed it on the first go!")
            break
        else:
            print(f"Congrats, you guessed the number in only {guesses} guesses!")
    elif guess < num:
        print("That guess was too low, try a higher number.\n")
    elif guess > num:
        print("That guess was too high, try a lower number.\n")
    else:
        print("Not sure how we even got here as it shouldnt be possible\n")



