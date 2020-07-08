print("This is a simple game which allows you to walk on a map. ")

locations = {0: "You are in hell... Good bye!", 1: "You are at the road.", 2: "You are at the mountain.",
             3: "You are in your house.", 4: "You are at the village.", 5: "You are in the forest."}

exits = [{"Q": 0}, {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0}, {"N": 5, "E": 1, "S": 4, "Q": 0}, {"W": 1, "Q": 0},
         {"N": 1, "W": 2, "Q": 0}, {"W": 2, "S": 1}]


loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())
    print(locations[loc])
    if loc == 0:
        break
    direction = input("Available exits are " + available_exits + " ").upper()
    print()
    if direction in exits[loc]:
        loc = exits[loc][str(direction)]
    else:
        print("You can't go to that direction! ")
