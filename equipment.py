import random
import csv

with open('scavenge.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)  # skip header
    items = [(item, level, category, secondary) for item, level, category, secondary in reader]

# Choose a random level 0 item
item_1 = random.choice([(item, level, category, secondary) for item, level, category, secondary in items if level == '0'])

# Choose a random item from any level
item_2 = random.choice(items)

# 25% chance to add a 3rd item
if random.random() < 0.25:
    item_3 = random.choice(items)
    # 25% chance to add a 4th item if there's a 3rd item
    if random.random() < 0.25:
        item_4 = random.choice(items)
        print(f"You found:\n{item_1[0]} ({item_1[1]}, {item_1[2]}{', ' + item_1[3] if item_1[3] else ''})\n{item_2[0]} ({item_2[1]}, {item_2[2]}{', ' + item_2[3] if item_2[3] else ''})\n{item_3[0]} ({item_3[1]}, {item_3[2]}{', ' + item_3[3] if item_3[3] else ''})\n{item_4[0]} ({item_4[1]}, {item_4[2]}{', ' + item_4[3] if item_4[3] else ''})")
    else:
        print(f"You found:\n{item_1[0]} ({item_1[1]}, {item_1[2]}{', ' + item_1[3] if item_1[3] else ''})\n{item_2[0]} ({item_2[1]}, {item_2[2]}{', ' + item_2[3] if item_2[3] else ''})\n{item_3[0]} ({item_3[1]}, {item_3[2]}{', ' + item_3[3] if item_3[3] else ''})")
else:
    print(f"You found:\n{item_1[0]} ({item_1[1]}, {item_1[2]}{', ' + item_1[3] if item_1[3] else ''})\n{item_2[0]} ({item_2[1]}, {item_2[2]}{', ' + item_2[3] if item_2[3] else ''})")
