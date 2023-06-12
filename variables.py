#Let's start a pizza parlor together! We're going to build a pizza parlor using some new Python programming concepts!!

#Let's build robot Cashier

#Greet customer
print("\nHello, welcome to 0xSamuel Pizza!!!!!!!\n")

#Ask for customer name
name = input("What is your name?\n")

#Greet customer w/ name and thank them for coming
if name == "Ben":
    evil_status = input("Are you evil?\n")
    if evil_status == "Yes":
        print("You're not welcome here Evil Ben!! Get out!!")
        exit()
    else:
        print("Oh, so you're one of those good Bens. Come on in!!")
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n")

#Pizza Menu
menu = "Personal Pizza, Medium Pizza, Large Pizza, XL Pizza"

#Ask customer what they want from menu
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

#Ask customer how many pizzas they want
quantity = input("How many pizzas would you like?\n")

#Set the price for pizza

if order  == "XL Pizza":
    price = 20
elif order == "Large Pizza":
    price = 16
elif order == "Medium Pizza":
    price = 12
elif order == "Personal Pizza":
    price = 8
else:
    print("Sorry, we don't have that here.")
    price = 0

print(price)

total = price * int(quantity)

print("Thank you. Your total is: $" + str(total))

print("Sounds good " + name + ", we'll have your " + quantity + " " + order + " ready for you in 10-15 minutes.\n")

