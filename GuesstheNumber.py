import random

def guesstheNumber(ending_range):
    random_number = random.randint(1, ending_range)
    guess = 0
    while guess != random_number:
        guess = int(input("Enter a number between 1 and " + str(ending_range) + " : "))
        if guess > random_number:
            print("sorry! try again the guess is too high")
        elif guess < random_number:
            print("sorry! try again the guess is too low")


    print("Yes, you have guessed the number "+ str(random_number) + " corretly")

guesstheNumber(10)