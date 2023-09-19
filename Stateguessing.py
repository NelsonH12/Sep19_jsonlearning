import json
import random

# Open the JSON file for reading
with open("data.json", "r") as json_file:
    data = json.load(json_file)

# Extract the state data from the loaded JSON
state = random.choice(list(data.keys()))  # Select a random state to guess
attributes = data[state]
clues = list(attributes.values())
random.shuffle(clues)  # Shuffle the order of clues

attempts = len(clues)  # Set the number of attempts based on the number of clues

print(f"Welcome to the State Guessing Game! You have {attempts} clues to guess the state.")

while attempts > 0:
    print(f"Clue {len(clues) - attempts + 1}: {clues.pop(0)}")  # Provide a structured clue
    user_guess = input("Your guess: ").strip().lower()

    if user_guess == state.lower():  # Convert the state name to lowercase for comparison
        print(f"Congratulations! You guessed correctly. It's {state}.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Incorrect guess. You have {attempts} clues left.")
        else:
            print(f"Out of clues! The answer is {state}.")
