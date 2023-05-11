


def delivery():
    packages = input("packages delivered: ")
    collisions = input("collisions occured: ")

    points = (50 * int(packages)) - (10 * int(collisions))
    if packages >= collisions:
        points += 500

    print(f"there were {packages} packages and {collisions} collisions. you earned {points} points")

delivery()