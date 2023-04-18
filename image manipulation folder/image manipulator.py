from PIL import Image
import os

image1 = Image.open('image manipulation folder/bingus.jpeg')

#image1.show()

def jpeg_to_png(): #DONE
    file_name = input("enter the filename) \nexample: bingus.jpeg \n\nchosen image: ")
    try:
        image_old = Image.open("image manipulation folder/" + str(file_name))
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[1] | yes \n[2/any] | no \ninput: ")
        match error_prompt:
            case "1": jpeg_to_png
            case _: quit

    try:
        os.mkdir("image manipulation folder/png images")
        #pass
    except:
        pass #don't do anything if there is already a "png images" folder

    try:
        image_old.save("image manipulation folder/png images/" + (file_name.replace("jpeg", "png")))
        #pass
    except:
        pass #don't do anything if the png file already exists
    end()

def change_size(): # DO TOMORROW
    thumb_200 = (200, 200)
    thumb_400 = (400, 400)
    thumb_600 = (600, 600)

    image_size = Image.open("image manipulation folder/" + str(input("enter the filename) \nexample: bingus.jpeg \n\nchosen image: ")))
    image_size.show()
    

    size_choice : int = 0
    while size_choice <= 0 and size_choice < 4:
        size_choice = int(input("what thumbnail size would you like to change this to? \n\noptions: \n[1] | size 200 \n[2] | size 400 \n[3] | size 600"))
        match size_choice:
            case 1: 
                image_size.thumbnail(thumb_200)
                image_size.save("image manipulation folder/" + image_size.replace(".jpeg", "(200).png"))
            case 2: 
                image_size.thumbnail(thumb_400)
                image_size.save("image manipulation folder/" + image_size.replace(".jpeg", "(400).png"))
            case 3: 
                image_size.thumbnail(thumb_600)
                image_size.save("image manipulation folder/" + image_size.replace(".jpeg", "(600).png"))

    #image_size.save("image manipulation folder/" + file_name.replace(".jpeg", "(200).png"))
    
    end()

def blur_image():
    print("set to mode 3")
    end()

def black_white():
    print("set to mode 4")
    end()

def rotate_image():
    try: 
        file_name = input("enter the filename) \nexample: bingus.jpeg \n\nchosen image: ")
        image_rotate = Image.open("image manipulation folder/" + str(file_name))
        #image_rotate = Image.open("image manipulation folder/" + str(input("enter the filename) \nexample: bingus.jpeg \n\nchosen image: ")))
        degree = None
        while type(degree) is not int:
            degree = int(input("how many degrees would you like to rotate this image?: "))
        image_rotate.rotate(degree).save("image manipulation folder/" + file_name.replace(".jpeg", "(rotated).jpeg"))
    except:
        print("error 3")
        return 3

    
    end()

def view_image(): #DONE
    try: 
        image_view = Image.open("image manipulation folder/" + str(input("enter the filename) \nexample: bingus.jpeg \n\nchosen image: ")))
        image_view.show()
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[   1   ] | yes \n[2 / any] | no \ninput: ")
        match error_prompt:
            case "1": view_image
            case _: quit
    end()

def end(): #DONE
    input_choice = 0
    print("\nchoice reset")
    
    input_choice = input("would you like to continue image manipulating? \n[ 1 ] | yes \n[any] | no/quit \nselect a value: ")
    match input_choice:
        case "1": start_menu()
        case _: quit

def start_menu():
    input_choice = 0
    while input_choice > 6 or input_choice < 1:
        input_choice = int(input("Welcome to the image manipulator! What Would you like to do? \n[1] | convert to png \n[2] | change thumbnail size \n[3] | blur an image \n[4] | change to black n' white \n[5] | rotate an image \n[6] | view an image \n\nSelect a value designated to a function: "))
    # -----------------------------------------------------------
    if input_choice == 1: jpeg_to_png()
    elif input_choice == 2: change_size()
    elif input_choice == 3: blur_image()
    elif input_choice == 4: black_white()
    elif input_choice == 5: rotate_image()
    elif input_choice == 6: view_image()
    else: print("error 1"); return 1

start_menu()





"""
the project requirements:

[png] // Every png file saved will be moved here ===================================================== DONE
[size 200] // every file saved with this thumbnail size will be sent here -- SET UP
[size 400] // every file saved with this thumbnail size will be sent here -- SET UP
[size 600] // every file saved with this thumbnail size will be sent here -- SET UP
[rotated] // send every rotated file here -- SET UP
[black white] // send every black/white file here -- SET UP
No folder for blurred files -- SET UP
[custom change] // look at documentation and add a custom change with its folder
Have option to view every edited image 
Have no errors for whatever the user inputs on runtime
MUST have unique variable and folder names. ESPECIALLY CODE ========================================= DONE
BONUS: Have [hybrid] for pictures with multiple changes
BONUS: Have the script build the folders for you when a new change type is created
Expected inputs:

what would you like to do? [ action | [1] ] [ action 2 | [2] ] [ etc... | [3] ] : input if error: invalid input. Try again > what would you like to do? [ action | [1] ] [ action 2 | [2] ] [ etc... | [3] ] : input_corrected if no folder: create folder [input] send to [input] else: send to [input]

w at


"""