from random import randint

finished = False
guess = 0
guesses = 0


def gen_rand_number():
    return randint(1, 101)

def check_number(guess):
    return guess == num

def advise_user():
        if guess < num:
            print("That guess was too low, try a higher number.\n")
        if guess > num:
            print("That guess was too high, try a lower number.\n")

num = gen_rand_number()

while not finished:
    try:
        guess = int(input(f"Please guess a number between 1 and 100 (guess {guesses}): "))
    except:
        print("Im going to guess you didnt enter a number")

    guesses += 1

    if guess not in range(1,101):
        print("That guess was outside of the range, its only between 1 and 100\n")
    elif check_number(guess):
        finished == True
        if guesses == 1:
            print("Wow, you guessed it on the first go!")
            break
        else:
            print(f"Congrats, you guessed the number in only {guesses} guesses!")
    else:
        advise_user()



