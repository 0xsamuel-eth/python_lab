#Let's learn about lists and methods

#What is a Python Method?
#A function that is available for a given object b/c of the object's type

supplies = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

camp_site = ["Crystal Lake", 404, 95.5, 10, False]

#supplies.append("toilet paper")

#supplies.extend("toilet paper", "bidet")

supplies.insert(0, "bidet")

#Add an item to second to last location in list
supplies.insert(-1, "toilet paper")

print(supplies)

