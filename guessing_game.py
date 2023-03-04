import random

"""
Note: Chapter 3 answers are written as comments below the script
"""

def game(prompt):
    range_num = 0
    while range_num <= 0: # a while loop that ends until a positive int is given as a range
        try:
            range_num = int(input("setup: choose a range - "))
        except:
            continue
            # range_num = 100
    guessed_num = None
    magic_num = None
    
    match prompt:
        case "computer guess":
            magic_num = int(input(f"pick a whole number between 0-{range_num}: "))
            user_prompt = ""
            min_value = 1
            max_value = range_num
            while True:
                guessed_num = (random.randint(min_value, max_value))
                user_prompt = input(f"Computer guessed {guessed_num}. Is it too high, too low, or correct? (h, l, c): ")
                match user_prompt:
                    case "c": 
                        break
                    case "h":
                        max_value = guessed_num - 1
                    case "l":
                        min_value = guessed_num + 1 
            print("computer successfully guessed the number")

        case "user guess": 
            magic_num = random.randrange(range_num)
            #diff_guessed = None
            print(f"the number is between 0-{range_num} ")
            while guessed_num != magic_num:
                try:
                    guessed_num = int(input("guess the number: "))
                except:
                    continue # loop again if input not given
                if guessed_num > magic_num:
                    print("too high")
                elif guessed_num < magic_num:
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



"""
Chapter 3 Answers
--------------------
1. The benefits of a function
    a. Helps reduce the need of copy pasting
    b. Use less lines to write a program
    c. Makes code cleaner looking
2. Executing a function
    It is only executed when you call it. It is never executed right when it is
    given a meaning- *defined* in this case
3. Defining a function
    Use the keyword "def" followed by function name and parantheses, then end with a colon
    Ex. 
        def function_name():
            pass #replace pass with your block of code

4. The function represents a block of code written for a specific purpose. A function call however
   is essentially you telling the program to USE that code
***5. There is only ONE global scope. There are multiple local scopes that can be present at once however.
6. A local scope is created whenever a function is called. The local scope is destroyed along with the variables in it once the function returns a value
7. A return value can be described as certain information given from a function. 

   Return values can also be used in expressions
      Ex. 
      def cube(num):
         return num * num * num
      some_number = 3
      print(cube(sum_number) + 4) 
      Inside the print statement, we are adding 4 to a function call. This works because we are adding 4 to whatever value is returned to the function call

8. If you don't return anything, the function on default returns none
9. To give a function the ability to edit a global function, write the global keyword followed by the name of the global variable wanted
10.The none value represents *no value* or an empty value, similar to Null. It is a "nonetype".
***11.
12.After importing spam:
   spam.bacon()
13.Errorhandling keeps a program running even when it gets an error (exception), by running a different block of code using the try and except keywords
14.The try clause runs a block of code under it and makes sure it doesn't generate an error. when an error pops up however, it tests out what's under the except clause.
   these two are great if you want to keep a program running even when an error happens

"""