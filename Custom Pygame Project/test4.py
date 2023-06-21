# practice section
x = "HHHHHHH"

#sequence = input("what sequence do you want to check in a string? ")

#print(x.count(sequence))

# -------------

num_happy = 0
num_sad = 0

sad_face = ":^("
happy_face = ":^)"
sentence = input("write the input with \":^)\" and/or \":^(\": ")

print(f"sad: {sentence.count(sad_face)}")
print(f"happy: {sentence.count(happy_face)}")

if sad_face == happy_face:
    print("mood: neutral")
elif sad_face > happy_face:
    print("mood: sad")
elif sad_face < happy_face:
    print("mood: happy")
else:
    print("none")