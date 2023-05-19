import random

# Get the name of the roll
roll_name = input("What are we rolling? ")

# Get the starting value
starting_value = int(input("Starting value? "))

# Create a list of characters
characters = ["Travvy", "Ashley", "Ned", "Digby", "Theo", "Wil", "Kurt", "Maria", "Claude"]

print(f"Rolling versus {roll_name} ({starting_value}):")

# Roll the dice for each character
for character in characters:
    rolls = []
    for i in range(2):
        rolls.append(random.randint(1, 6))

    successes = starting_value
    for roll in rolls:
        if roll == 5 or roll == 6:
            successes += 1
        elif roll == 1:
            successes -= 1

    # Print the roll results
    print(f"{character} {rolls} =  {successes}")
