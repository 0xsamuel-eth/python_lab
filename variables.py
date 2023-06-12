#Let's start a pizza parlor together! We're going to build a pizza parlor using some new Python programming concepts!!

#Let's build robot Cashier

#Greet customer
print("\nHello, welcome to 0xSamuel Pizza!!!!!!!\n")

#Ask for customer name
name = input("What is your name?\n")

#Greet customer w/ name and thank them for coming
if name == "Ben":
    print("You're not welcome here Evil Ben!! Get out!!")
    exit()
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n")


#Pizza Menu
menu = "Personal Pizza, Medium Pizza, Large Pizza, XL Pizza"

print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu)

order = input()

price = 12

quantity = input("How many pizzas would you like?\n")

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in 10-15 minutes.\n")

