#Let's learn about lists and methods

#What is a Python Method?
#A function that is available for a given object b/c of the object's type

supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 95.5, 10, False]

#supplies.append("toilet paper")
#supplies.insert(0, "bidet")

#Adding an item to second to last location in list
#supplies.insert(-1, "toilet paper")

supplies.extend(["toilet paper", "bidet"])

#Remove entire list
#supplies.clear()

#supplies.remove("tent")
#supplies.remove("sleeping bags")

print("This item was just deleted: " + supplies.pop(0))
supplies.pop(0)

print(supplies)

