import random


def rps7(rounds):
    global tally
    tally = [0, 0] # tally[user, computer]
    for counter in range(rounds):
        user = input("choose an element: s (scissors), r (rock), v (velociraptor), l (lizard), p (paper), k (spock), h (hawking): ")
        computer = random.randrange(7)
        match computer:
            case 0: computer = "s"
            case 1: computer = "r"
            case 2: computer = "v"
            case 3: computer = "l"
            case 4: computer = "p"
            case 5: computer = "k"
            case 6: computer = "h"
            case _: print("error 1"); return 1

        print(f"computer: {computer}")
        print(f"user: {user}")

        if user == computer: print('\033[1;36m' + "tied" + '\033[0m') 
        else:
            match user:
                case "s":
                    if computer == "p" or computer == "h" or computer == "l":
                        #global tally
                        tally[0] += 1
                        print('\033[1;32m' + "you won" + '\033[0m') 
                    else:
                        tally[1] += 1
                        print('\033[1;31m' + "you lost" + '\033[0m') 
                case "r":
                    if computer == "s" or computer == "l" or computer == "h":
                        #global tally
                        tally[0] += 1
                        print('\033[1;32m' + "you won" + '\033[0m') 
                    else:
                        tally[1] += 1
                        print('\033[1;31m' + "you lost" + '\033[0m') 
                case "v":
                    if computer == "s" or computer == "r" or computer == "h":
                        #global tally
                        tally[0] += 1
                        print('\033[1;32m' + "you won" + '\033[0m') 
                    else:
                        tally[1] += 1
                        print('\033[1;31m' + "you lost" + '\033[0m') 
                case "l":
                    if computer == "v" or computer == "k" or computer == "p":
                        #global tally
                        tally[0] += 1
                        print('\033[1;32m' + "you won" + '\033[0m') 
                    else:
                        tally[1] += 1
                        print('\033[1;31m' + "you lost" + '\033[0m') 
                case "k":
                    if computer == "v" or computer == "r" or computer == "s":
                        #global tally
                        tally[0] += 1
                        print('\033[1;32m' + "you won" + '\033[0m') 
                    else:
                        tally[1] += 1
                        print('\033[1;31m' + "you lost" + '\033[0m') 
                case "h":
                    if computer == "k" or computer == "p" or computer == "l":
                        #global tally
                        tally[0] += 1
                        print('\033[1;32m' + "you won" + '\033[0m') 
                    else:
                        tally[1] += 1
                        print('\033[1;31m' + "you lost" + '\033[0m') 
                case _:
                    print("error: user selected invalid character ")
                    print("program ended")
                    print(" ")
                    return 1
        print(f"tries: {counter}")
        print(" ")
    print(f"user score: {tally[0]}")
    print(f"computer score: {tally[1]}")

    match input("would you like to play again? "):
        case "y": 
            b = int(input("how many rounds would you like to play?: "))
            rps7(b)
        case _: quit
    return 0

def start_game():
    match input("would you like to play rock paper scissors 7? (y/n): "):
        case "y":
            a = int(input("how many rounds would you like to play?: "))
            rps7(a)
        case "n":
            quit
        case _:
            start_game()
    return 0

start_game()


"""
CHAPTER 4 ANSWERS

1. What is []?
    It is a list
2. Assigning hello as a third list value
    a = [2, 4, 6, 8, 10]
    a[2] = "hello"
    print(a) #prints out [2, 4, "hello", 8, 10] #replaces value at a[2]
3. 
    '3' is a string, multiplying it by 3 makes '33'. Convert it to an int and it becomes 33- which is then divided by 11 giving us 3, in index 3, the element is 'd'
4. 
    spam[-1] refers to the very last element, which is 'd'

5. evaluates to 'b'. Referes to the first value checked that matches the value inputed into index()

6. It evaluated to index 1

7. It adds the int value 99 at the end of the list
    it looks like this:
        [3.14, 'cat', 11, 'cat', True, 99]
8. It removes the first element valued 'cat'
    It looks like this:
        [3.14, 11, 'cat', True]
9.  List Concatenation: + ---> list + another_list
    list replication: * ----> list * 3 

10. With append(), you can only add elements at the very end (as in- index -1). 
    With insert() however.. you have the freedom to specify at what index to place your element, 
    shifting other elements after it

11. both del() and remove() can remove values from a list
12. 
    Strings are actually "lists" of characters. They both can be looped through
    ex. 
        for i in "string of text"
            print(i)
        for i in some_list
            print(i)
    you can use the "in" keyword for both strings and lists
        if <<element>> in "string text":
            <<code block>>
        if <<different_element>> in some_list:
            <<code block>>
13.
    A list's elements can be changed after declaring them. Tuples however, cannot have their
    elements changed after declaration
14. Similar to lists but with one small change
    some_tuple()
15. You can convert lists and tuples just as you would with int() or str() 
    ---> list() and tuple()
16. List variables don't contain the actual list- rather they contain the references of that list's values
17. copy.copy() creates a duplicate version of a list. Both versions have their own references.
    However, what if a list had an inner list? Using copy.copy(), it will only copy the reference to that inner list. 
    (if you change an inner list in one of the given lists, it will affect the other list)
    
    Deep copy however is able to create a copy of that inner list with a different reference

    """