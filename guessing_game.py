import random

def game(prompt):
    range_num = 0
    while range_num <= 0: # a while loop that ends until a positive int is given as a range
        try:
            range_num = int(input("setup: choose a range - "))
        except:
            continue
            # range_num = 100
    match prompt:
        case "computer guess":
            number = int(input(f"pick a whole number between 0-{range_num}: "))
            if number > range_num:
                quit
            guessed = (random.randrange(range_num + 1)) # Program generates value a maximum of range_num - 1. The + 1 in the randrange() was used to counter that
            print(f"the computer guessed {guessed}")
            if guessed != number:
                print("the numbers don't match, you won!")
            else:
                print("the numbers matched, you lose!")

        case "user guess": 
            diff_number = random.randrange(range_num)
            diff_guessed = 0
            print(f"the number is between 0-{range_num} ")
            while diff_guessed != diff_number:
                try:
                    diff_guessed = int(input("guess the number: "))
                except:
                    continue # loop again if input not given
                if diff_guessed > diff_number:
                    print("too high")
                elif diff_guessed < diff_number:
                    print("too low")
            print("success")
    


    match input("restart program? (y/any different button to quit): "):
        case "y": a()
        case _: quit
            
def a():
    choice = input("select mode for number guessing game - (user guess/computer guess/q): ")
    match choice:
        case "computer guess": game("computer guess")
        case "user guess": game("user guess")
        case "q": quit
        case _: game("n")
a()
