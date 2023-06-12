#Let's start a pizza parlor together! We're going to build a pizza parlor using some new Python programming concepts!!

#Let's build robot Cashier

print("\nHello, welcome to 0xSamuel Pizza!!!!!!!\n")

name = input("What is your name?\n")

if name == "Ben":
    print("You're not welcome here Evil Ben!! Get out!!")
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n")

menu = "Personal Pizza, Medium Pizza, Large Pizza, XL Pizza"

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 12

quantity = input("How many pizzas would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in 10-15 minutes.\n")

