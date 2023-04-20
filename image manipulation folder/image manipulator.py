from PIL import Image
from PIL import ImageFilter
import os

#image1 = Image.open('image manipulation folder/bingus.jpeg')

#image1.show()

"""
NOTE:
--------------
This script uses Python version 3.11.3 with Pillow to work as intented


initial idea:

start()
    > user chooses out of x options
    > match based on user input
        a:
            view images
                > get filename from user
                > open file
        b:
            change thumbnail size
                > get filename from user
                > get user's preferred thumbnail size
                > set thumbnail size of image
                > save with selected thumbnail size
        c: 
            jpeg to pdf
                > get filename from user
                > save and convert to png by changing the filename to have ".png" at the end
        d: 
            make an image black and white
                > get filename from user
                > save and use filter (refer to video from class)
        e: 
            blur an image
                > get filename from user
                > save and use filter (refer to video from class) 
        f: 
            rotate an image
                > get filename from user
                > get amount of degrees to rotate
                > save and rotate with users input to rotate (refer to video from class)   

---------------------------------
What I could have been done to improve this project if I had more time:
    1. Could have moved duplicate code into their own functions to save lines (example: getting the file name and creating a directory) 
    2. Could have made code more *clean* to prevent new bugs from emerging
                
"""



def jpeg_to_png(): #VERIFIED
    file_name = input("enter the filename) \nexample: bingus.jpeg \n\nchosen image: ")
    try:
        image_old = Image.open("image manipulation folder/" + str(file_name))
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[1] | yes \n[2/any] | no \ninput: ")
        match error_prompt:
            case "1": jpeg_to_png
            case _: quit()

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

def change_size(): # DONE
    thumb_200 = (200, 200)
    thumb_400 = (400, 400)
    thumb_600 = (600, 600)

    try:
        file_name = input("enter the filename \nexample: bingus.jpeg \n\nchosen image: ")
        image_size = Image.open("image manipulation folder/" + str(file_name))
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[ 1 ] | yes \n[any] | no \ninput: ")
        match error_prompt:
            case "1": rotate_image()
            case _: 
                quit() #bug: if the parentheses are removed, it continues from here to ask how many degrees to rotate the image, despite not having the image detected
    
    size_choice = 0
    while  size_choice != "1" and size_choice != "2" and size_choice != "3":
        size_choice = (input("what thumbnail size would you like to change this to? \n\noptions: \n[1] | size 200 \n[2] | size 400 \n[3] | size 600\n\n input: "))
        match size_choice:
            case "1": 
                image_size.thumbnail(thumb_200)
                try:
                    os.mkdir("image manipulation folder/size 200")
                except:
                    pass

                image_size.save("image manipulation folder/size 200/" + file_name.replace(".jpeg", "(200).jpeg"))
            case "2": 
                image_size.thumbnail(thumb_400)
                try:
                    os.mkdir("image manipulation folder/size 400")
                except:
                    pass

                image_size.save("image manipulation folder/size 400/" + file_name.replace(".jpeg", "(400).jpeg"))
            case "3": 
                image_size.thumbnail(thumb_600)
                try:
                    os.mkdir("image manipulation folder/size 600")
                except:
                    pass

                image_size.save("image manipulation folder/size 600/" + file_name.replace(".jpeg", "(600).jpeg"))
            case _:
                print(image_size)
    #image_size.save("image manipulation folder/" + file_name.replace(".jpeg", "(200).png"))
    
    end()

def blur_image(): #BUGGED
    try:
        file_name = input("enter the filename \nexample: bingus.jpeg \n\nchosen image: ")
        image_blur = Image.open("image manipulation folder/" + str(file_name))
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[ 1 ] | yes \n[any] | no \ninput: ")
        match error_prompt:
            case "1": blur_image()
            case _: 
                quit() 
    try:
        os.mkdir("image manipulation folder/blurred images")
    except:
        pass 

    try: 
        blur_value = int(input("how much do you want to blur your image  \n\npick a number: ")); 
    except: 
        error_prompt = input("your input is invalid. would you like to retry this function? \n[ 1 ] | yes \n[any] | no \n\ninput: ")
        match error_prompt:
            case "1": blur_image()
            case _: 
                quit() 
    
    try:
        image_blur.filter(ImageFilter.GaussianBlur(blur_value)).save("image manipulation folder/blurred images/" + "e.jpeg") # It appears to me that the interpreter cannot find the "ImageFilter" class. 
    except:
        print("cannot save file with blur function properly")
    end()

def black_white(): #DONE
    try:
        file_name = input("enter the filename \nexample: bingus.jpeg \n\nchosen image: ")
        image_colorless = Image.open("image manipulation folder/" + str(file_name))
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[ 1 ] | yes \n[any] | no \ninput: ")
        match error_prompt:
            case "1": black_white()
            case _: 
                quit() 
    try:
        os.mkdir("image manipulation folder/black-white images")
    except:
        pass 

    try:
        image_colorless.convert(mode= 'L').save("image manipulation folder/black-white images/" + (file_name.replace(".jpeg", "(colorless).jpeg")))
    except:
        pass
    end()

def rotate_image(): #DONE
    try:
        os.mkdir("image manipulation folder/rotated images")
    except:
        pass #pass anything if folder already exists
    
    try: 
        file_name = input("enter the filename \nexample: bingus.jpeg \n\nchosen image: ")
        image_rotate = Image.open("image manipulation folder/" + str(file_name))
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[ 1 ] | yes \n[any] | no \ninput: ")
        match error_prompt:
            case "1": rotate_image()
            case _: 
                quit() #bug: if the parentheses are removed, it continues from here to ask how many degrees to rotate the image, despite not having the image detected
    degree = None
    while type(degree) is not int:
        degree = int(input("how many degrees would you like to rotate this image?: "))
    
    image_rotate.rotate(degree).save("image manipulation folder/rotated images/" + file_name.replace(".jpeg", "(rotated["+ str(degree) +"]).jpeg"))
    end()

def view_image(): #DONE
    try: 
        image_view = Image.open("image manipulation folder/" + str(input("enter the filename) \nexample: bingus.jpeg \n\nchosen image: ")))
        image_view.show()
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[   1   ] | yes \n[2 / any] | no \ninput: ")
        match error_prompt:
            case "1": view_image
            case _: quit()
    end()

def transpose_image(): #TEST
    try: 
        file_name = input("enter the filename \nexample: bingus.jpeg \n\nchosen image: ")
        image_transpose = Image.open("image manipulation folder/" + str(file_name))
    except:
        error_prompt = input("it looks like there is no existing file in this directory. Would you like to try again? \n\n[ 1 ] | yes \n[any] | no \ninput: ")
        match error_prompt:
            case "1": transpose_image()
            case _: 
                quit()
    try:
        os.mkdir("image manipulation folder/transposed images")
    except:
        pass

    transpose_choice = None
    while transpose_choice != "1" and transpose_choice != "2" and transpose_choice != "3" and transpose_choice != "4" and transpose_choice != "5":
        transpose_choice = input("how would you like to transpose your image? \n[1] | flip horizontally \n[2] | flip vertically \n[3] | rotate 90 degrees \n[4] | rotate 180 degrees \n[5] | rotate 270 degrees \n\n input: ")
    
    match transpose_choice:
        case "1":
            image_transpose.transpose(Image.Transpose.FLIP_LEFT_RIGHT).save(f"image manipulation folder/transposed images/{file_name}")
        case "2":
            image_transpose.transpose(Image.Transpose.FLIP_TOP_BOTTOM).save(f"image manipulation folder/transposed images/{file_name}")
        case "3":
            image_transpose.transpose(Image.Transpose.ROTATE_90).save(f"image manipulation folder/transposed images/{file_name}")
        case "4":
            image_transpose.transpose(Image.Transpose.ROTATE_180).save(f"image manipulation folder/transposed images/{file_name}")
        case "5":
            image_transpose.transpose(Image.Transpose.ROTATE_270).save(f"image manipulation folder/transposed images/{file_name}")
    end()

def end(): #DONE
    input_choice = 0
    print("\nchoice reset")
    
    input_choice = input("would you like to continue image manipulating? \n[ 1 ] | yes \n[any] | no/quit \nselect a value: ")
    match input_choice:
        case "1": start_menu()
        case _: quit()

def start_menu(): #DONE
    input_choice = 0
    while input_choice > 7 or input_choice < 1:
        input_choice = int(input("Welcome to the image manipulator! What Would you like to do? \n[1] | convert to png \n[2] | change thumbnail size \n[3] | blur an image \n[4] | change to black n' white \n[5] | rotate an image \n[6] | view an image \n[7] | transpose an image \n\nselect a value designated to a function: "))
    # -----------------------------------------------------------
    if input_choice == 1: jpeg_to_png()
    elif input_choice == 2: change_size()
    elif input_choice == 3: blur_image()
    elif input_choice == 4: black_white()
    elif input_choice == 5: rotate_image()
    elif input_choice == 6: view_image()
    elif input_choice == 7: transpose_image()
    else: print("error 1"); return 1

start_menu()





"""
the project requirements:

[png] // Every png file saved will be moved here ===================================================== DONE
[size 200] // every file saved with this thumbnail size will be sent here ============================ DONE
[size 400] // every file saved with this thumbnail size will be sent here ============================ DONE
[size 600] // every file saved with this thumbnail size will be sent here ============================ DONE
[rotated] // send every rotated file here ============================================================ DONE
[black white] // send every black/white file here ==================================================== DONE
No folder for blurred files ==================================== FIX IMAGE FILTER MODULE ERROR
[custom change] =====================================================Transpose an image=============== DONE
Have option to view every edited image -------------- ?????
Have no errors for whatever the user inputs on runtime =============================================== Hit or miss





MUST have unique variable and folder names. ESPECIALLY CODE ========================================== DONE (but super messy)
BONUS: Have the script build the folders for you when a new change type is created ==== mostly done===





BONUS: Have [hybrid] for pictures with multiple changes - this feature has not been implemented

w at
"""
