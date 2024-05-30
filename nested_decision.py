# Task 1: Code Correction

#place = input("Choose a place: forest or cave? ")

#if place == "forest":
#    action = input("climb a tree or cross a river?")
#    if action == "climb a tree":
#        print("You found a bird's nest!")
#    elif action == "cross a river":
#        print("You found a boat!")
#elif place == "cave":
#    print("You find a hidden treasure!")

# Task 1 is commented out because of task 2 and 3

# Task 2: Setting the Scene


#place = input("Choose a place: forest or cave? ")

#if place == "forest":
#    action = input("climb a tree or cross a river?")
#    if action == "climb a tree":
#        print("You found a bird's nest!")
#    elif action == "cross a river":
#        print("You found a boat!")
#elif place == "cave":
#    action_2 = input("Do you want to: light a torch or proceed in the dark ")
#    if action_2 == "light a torch":
#        print("Well done. You can see better!")
#    elif action_2 == "proceed in the dark":
#        print("Good luck trying to see")

# Task 1 & 2 is commented out because of task 3

# Task 3: Default Path

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
         pass
elif place == "cave":
    action_2 = input("Do you want to: light a torch or proceed in the dark ")
    if action_2 == "light a torch":
        print("Well done. You can see better!")
    elif action_2 == "proceed in the dark":
        print("Good luck trying to see")
    else:
         pass
