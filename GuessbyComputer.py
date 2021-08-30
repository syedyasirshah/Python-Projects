import random

def computer_guess(ending_range):
    low = 1
    high = ending_range
    feedback = " "
    while feedback != "c":
        if low != high:
          guess = random.randint(low, high)
        else:
            guess = low
        feedback = input("Is the number " + str(guess) + " is too high (h), too low (l) or is it correct (c): ")
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1


    print("Thank God guess the number correctly!")

computer_guess(50)
