def choose_story():
    story_mode = input("Which story would you like? (choose 1/2/3 or q to quit): ")
    if story_mode == "q":
        quit
    else:
        start(int(story_mode))

def start(story_ID):
    noun = input("noun: ") #example -> a name, individual, etc..
    adjective = input("adjective: ") # example -> interesting, kind, weird, catchy
    plural_noun = input("plural noun: ") # example ->
    body_part = input("body part: ") # example ->
    number = input("number: ") # Self explanatory
    verb_in_ing = input("verb ending in \"ing\": ") # running, eating, etc..

    if story_ID == 1:
        print("chosen path 1")
        print(f"A knight named {noun} was trying to fight {number} {plural_noun} at once. They- in a fit of anger- give up and throw their {adjective} weapon. It hits one of the {plural_noun} {body_part}s and runs off never to be seen again. The last time they were seen was when they were {verb_in_ing}")
    elif story_ID == 2:
        print(f"{noun} was {verb_in_ing} until a paper cut-out of the number {number} flies smack-dab at their {body_part}. Bewildered, they grab the {adjective} paper and crumble it. It turns out a bunch of {plural_noun} were responsible for the paper flying at {noun}, and the {plural_noun} get ticked off and start booing at them")
    elif story_ID == 3:
        print(f"a bunch of {plural_noun}- around {number} of them were like \"hmm I wonder what happens if we start a {adjective}, neverending, while loop\". {noun} interrupts them before it was too late. ")
    else:
        print("Specified path unavailable, please try again")
        choose_story()


choose_story()
