print("*" * 38 , "\n")
print("**    Welcome to the Snakes Cafe!    **" )
print("**    Please see our menu below.    **")
print("**")
print("** To quit at any time, type \"quit\" **", "\n")
print("*" * 38)
print("\n", "\nAppetizers\n----------\n", "Wings\n", "Cookies\n", "Spring Rolls\n", "\n", "\n", "\nEntrees\n-------\n", "Salmon\n", "Steak\n" , "Meat Tornado\n", "A Literal Garden\n",  "\nDessets\n-------\n", "Ice Cream\n", "Cake\n", "Pie\n", "\n", "\nDrinks\n------\n", "Coffee\n", "Tea\n", "Unicorn\n", "\n", "\n", "*" * 35 , "\n** What would you like to order? **\n", "*" * 35,)
response = ""
order = {
    "Wings" : 0, 
    "Cookies" : 0,
    "Spring Rolls" : 0,
    "Salmon" : 0,
    "Steak" : 0,
    "Meat Tornado" : 0,
    "A Literal Garden" : 0,
    "Coffee" : 0,
    "Ice Cream" : 0,
    "Cake" : 0,
    "Pie" : 0,
    "Tea" : 0,
    "Unicorn" : 0,
    "quit" : 0
}


while response != "quit":
    response = input("> ")
    if response == "quit":
        break
    else:      
        order[response] += 1
        if order[response] > 1:
            print(f"** {order[response]} orders of {response} have been added to your meal **")
        else:
            print(f"** {order[response]} order of {response} have been added to your meal **")
