from PIL import Image

image1 = Image.open('image manipulation folder/bingus.jpeg')

#image1.show()

def to_png():
    print("set to mode 1")
    end()

def change_size():
    print("set to mode 2")
    end()

def blur_image():
    print("set to mode 3")
    end()

def black_white():
    print("set to mode 4")
    end()

def rotate_image():
    print("set to mode 5")
    end()

def end():
    input_choice = 0
    print("\nchoice reset")
    
    while input_choice > 2 or input_choice < 1:
        input_choice = int(input("would you like to continue image manipulating? \n[1] | yes \n[2] | no/quit \nselect a value: "))
    
    if input_choice == 1:
        start_menu()
    elif input_choice == 2:
        quit
    else:
        print("error 2")
        return 2

def start_menu():
    input_choice = 0
    while input_choice > 5 or input_choice < 1:
        input_choice = int(input("Welcome to the image manipulator! What Would you like to do? \n[1] | convert to png \n[2] | change thumbnail size \n[3] | blur an image \n[4] | change to black n' white \n[5] | rotate an image \n\nSelect a value designated to a function: "))
    # -----------------------------------------------------------
    if input_choice == 1: to_png()
    elif input_choice == 2: change_size()
    elif input_choice == 3: blur_image()
    elif input_choice == 4: black_white()
    elif input_choice == 5: rotate_image()
    else: print("error 1"); return 1

start_menu()





"""
the project requirements:

[png] // Every png file saved will be moved here
[size 200] // every file saved with this thumbnail size will be sent here
[size 400] // every file saved with this thumbnail size will be sent here
[size 600] // every file saved with this thumbnail size will be sent here
[rotated] // send every rotated file here
[black white] // send every black/white file here
No folder for blurred files
[custom change] // look at documentation and add a custom change with its folder
Have option to view every edited image
Have no errors for whatever the user inputs on runtime
MUST have unique variable and folder names. ESPECIALLY CODE
BONUS: Have [hybrid] for pictures with multiple changes
BONUS: Have the script build the folders for you when a new change type is created
Expected inputs:

what would you like to do? [ action | [1] ] [ action 2 | [2] ] [ etc... | [3] ] : input if error: invalid input. Try again > what would you like to do? [ action | [1] ] [ action 2 | [2] ] [ etc... | [3] ] : input_corrected if no folder: create folder [input] send to [input] else: send to [input]

w at


"""