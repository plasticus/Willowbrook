import random

# Define the lists of words to choose from
groups = ["survivor", "scavenger", "straggler", "wanderer", "outcast", "human"]
actions = ["digging through a dumpster", "trying to get into a building", "exiting a building with full bags", "fighting amongst themselves", "trying to hotwire a car", "talking on a radio while looking at us", "silently staring at us", "trying to hide"]
scream_actions = ["There's a skirmish between some Zed and some survivors", "A survivor has hurt themselves", "A survivor is hunkered down crying", "A survivor is caught in a Zed trap", "A survivor is trying to redirect a group of zed using a tamborine and shouting", "A Zed is caught in a trap", "Nothing to be seen, though."]
quiet_actions = ["frozen corpses with no markings", "violently dead corpses", "signs of a recent fight with no bodies to be seen", "it smells like death but nothing to see", "the group feels like they're being watched"]

# Roll a 1d3 to determine which scenario to use
scenario_roll = random.randint(1, 3)

if scenario_roll == 1:
    # Roll a 1d6 to determine the number of survivors
    num_survivors = random.randint(1, 6)

    # Choose a random word from the appropriate list
    if num_survivors > 1:
        group_word = random.choice(groups)
        sentence = f"You see a small group of {num_survivors} {group_word}s {random.choice(actions)}."
    else:
        group_word = random.choice(groups)
        sentence = f"You see a lone {group_word} {random.choice(actions)}."

elif scenario_roll == 2:
    group_word = random.choice(groups)
    scream_sentence = random.choice(scream_actions)
    sentence = f"The group hears a scream nearby. {scream_sentence.replace('survivor', group_word)}"

else:
    quiet_sentence = f"It's quiet out here. Too quiet. The entire group is unnerved by it. {random.choice(quiet_actions)}"
    sentence = quiet_sentence

# Print the sentence
print(sentence)
