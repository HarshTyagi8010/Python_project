#  what we are going to create.
#  how it works 
# Fake News Headline Generator - Pseudocode
# Project Overview
# A Python program that generates humorous fake news headlines by combining random elements from predefined lists.
# Pseudocode Steps
# 1. START the program ✓
# 2. IMPORT the 'random' module ✓
# 3. CREATE a list of Indian subjects
# Example: ["Shahrukh Khan", "Virat Kohli", "Nirmala Sitharaman", "A Mumbai Cab", "A Group of Monkeys"]
# 4. CREATE a list of Indian actions
# Example: ["launches", "cancels", "dances with", "eats", "declares war on"]
# 5. CREATE a list of Indian places or things
# Example: ["at Red Fort", "in his bedroom", "local train", "a plate of samosas", "inside Parliament", "at Ganga ghat"]
# 6. START a loop (use while loop) that keeps running until the user says "no"
# a. RANDOMLY choose one item from each list (subject, action, place)
# b. COMBINE the three chosen words into one sentence using string formatting
# Example format: "BREAKING: {subject} {action} {place}!"
# c. PRINT the final fake news headline
# d. ASK the user if they want to generate another headline (yes/no)
# e. IF user says "no", END the loop
# 7. PRINT a thank you message for using the Fake News Generator
# 8. END the program
# Expected Output Format
# BREAKING: Shahrukh Khan launches at Red Fort!
# Do you want another headline? (yes/no): yes

# BREAKING: A Group of Monkeys eats a plate of samosas!
# Do you want another headline? (yes/no): no

# Thank you for using the Fake News Generator!
# Key Programming Concepts Used

# Lists and list indexing
# Random module for random selection
# While loops for continuous execution
# String formatting for output
# User input handling
# Conditional statements for loop control

# 1. import the  random module
import random

# 2. create subjects 
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "A Group of Monkeys"
    "Prime minister Modi",
    "Auto Rickshaw Driver From Delhi" 
]
# 3. create actions
actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
    "fights with",
    "sings with"
]
# 4. create places
places_or_things = [
    "at Red Fort",
    "in his bedroom",
    "local train",
    "a plate of samosas",
    "inside Parliament",
    "at Ganga ghat",
    "in a crowded market",
    "on the streets of Mumbai",
    "at a cricket stadium"
]

# 5. start a loop that keeps running until the user says "no"
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place = random.choice(places_or_things)

    headline = f" BREAKING NEWS: {subject} { action} { place} "
    print("\n" + headline)
    
    user_input = input("\nDo you want another headline (yes/no)").strip().lower()
    # .strip() is used for removing unnecessary space  
    # .lower is used for converting the input yes or no in lower case 
    if user_input == "no":
        break 

    print("\nThank you for using the Fake News Generator!")

