def count_votes():
    try:
        num_votes = int(input(""))
    except:
        quit()
    sequence = str(input(""))
    num_A = 0 
    num_B = 0

    for i in range(num_votes):
        if sequence[i] == "A":
            num_A += 1
        elif sequence[i] == "B":
            num_B += 1
    if num_A == num_B:
        print("tie")
    elif num_A > num_B:
        print("A")
    elif num_A < num_B:
        print("B")
    
count_votes()