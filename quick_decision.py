# Task 1: Code Correction

attendees = int(input("Enter number of attendees: "))
venue = "large hall" 

print(venue if attendees > 100 else "conference room")

# Task 2: Catering Choices

users = input("Do you want vegetarian food?: yes or no ")
yes  = "Veggie Delight Caterers"

print("I recommend", yes if users == "yes" else "Gourmet Meals Caterers")