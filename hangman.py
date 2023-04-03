import random
import string
from hangman_words import word_pasta, word_all, word_people, word_objects

#MODIFICATION: ADDED THEMED WORD SETS ^^^

#when you import a file.. it actually runs it? For example, a print statement from the imported file will be executed

def get_valid_word(set):
    word = random.choice(set)
    while "-" in word or ' ' in word:
        word = random.choice(set)
    return word

    #this function may not have been necessary as all my words have no spaces or "-"


def start_modded():
    player_input = 0

    # choose the word set
    while player_input <= 0 or player_input >= 4:
        player_input = int(input("welcome to hangman. Select your theme | objects/people [1] | pasta [2] | all [3] | : "))
    match player_input:
        case 1:
            player_input = word_objects + word_people
        case 2:
            player_input = word_pasta
        case 3:
            player_input = word_all
    
    #now, get the word
    magic_word = get_valid_word(player_input).upper()

    magic_word_letters = set(magic_word) #has no repeated letters 
    alphabet = set(string.ascii_uppercase)
    already_used = set() #what has been already used

    while len(magic_word_letters) > 0:
        print(f"used letters: {already_used}")
        word_list = [letter if letter in already_used else '-' for letter in magic_word] 
        print("Current word: ", ' '.join(word_list))


        letter_guessed = input("guess a letter: ").upper()
        if letter_guessed in alphabet - already_used:
            already_used.add(letter_guessed)
            print("added to list of guessed letters")
            # add to the list of guessed letters

            if letter_guessed in magic_word_letters:
                magic_word_letters.remove(letter_guessed)
                print("you got one of the letters!")
            # if this guessed letter is one of the magic word's letters,remove that letter from it's list
    
        elif letter_guessed in already_used:
            print("this character has already been used. Try a different character")

        else:
            print("the word does not contain this letter")
    print(f"you got the the word: {magic_word}")

start_modded()

