""" 
Test 1: Text messages

CU -> See you
:^) -> Im sad
:^( -> Im sad
:P -> Stick out my tongue


"""

translation = ["see you", "im happy", "im sad", "wink", "stick out my tongue", "sleepy", "totally awesome", "canadian computing competition", "because","thank you", "you're welcome", "talk to you later / text you later"]


def translator2():
    word2 = input("whats the word?: ").lower()

    if word2 == "cu": print(translation[0])
    elif word2 == ":)": print(translation[1])
    elif word2 == ":(": print(translation[2])
    elif word2 == ";)": print(translation[3])
    elif word2 == ":p": print(translation[4])
    elif word2 == "(`.`)": print(translation[5])
    elif word2 == "ta": print(translation[6])
    elif word2 == "ccc": print(translation[7])
    elif word2 == "cuz": print(translation[8])
    elif word2 == "ty": print(translation[9])
    elif word2 == "yw": print(translation[10])
    elif word2 == "ttyl": print(translation[11])
    else:
        print(word2)

    match input("Translate again?: [press 1 to redo, and any other button to quit]: "):
        case "1": translator2()
        case _: quit



translator2()



# BUGGED CODE
def translator1(): #Fixed version is above
    word = str(input("write the translation: "))
    
    match word:
        case "CU": print(translation[0])

        case ":-)": print(translation[1]) #bugged

        case ":(": print(translation[2]) #bugged
        
        case ";-)": print(translation[3]) #bugged
        
        case ":P": print(translation[4]) #bugged
        
        case "(`.`)": print(translation[5])
        case "TA": print(translation[6])
        case "CCC": print(translation[7])
        case "CUZ": print(translation[8])
        case "TY": print(translation[9])
        case "YW": print(translation[10])
        case "TTYL": print(translation[11])
        case _:
            print("no such translation available")
            translator1()
    match input("Translate again?: "):
        case "1": translator1()
        case _: quit
