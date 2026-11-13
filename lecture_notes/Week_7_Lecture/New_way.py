squawk = "\nTell me something, and I will repeat it to you:"
squawk += "\nEnter 'quit' to end the program. \n"

active = True 
while active:
    message = input(squawk)
    if message == 'quit': 
        active = False
    else:
        print("\n")
        print(message)

squawk = "\n Type in one item at a time, anyting you would like to add to the shopping list: " 
squawk += "\nEnter 'quit' when you are finished\n"
shopping_list = [] #used to have a list that the items typed will be put

while True:
    shop_list = input(squawk) #This prints the question that is in "squawk"
    if shop_list == 'quit': #If the user types 'quit' it will break the while loop
        break #breaks it out of the loop
    elif shop_list == 'list': #If 'list' is typed it will print the list using a for loop
        print("\nYour list contains:")
        for item in shopping_list:
            print(item.title())
    
    else: #Anything else will be considered an item for the shopping list
        shopping_list.append(shop_list) #This is how the items are placed into the shopping list
        print("\n")
        print(f"{shop_list.title()} has beed added to the shopping list!") 

print("\n")

currnet_nummber = 0
while currnet_nummber < 10:
    currnet_nummber += 1
    if currnet_nummber %2 == 0:
        continue
    print(currnet_nummber)

print("\n")

unconfirmed_models = ['T-800','T-1000','Marvin']
confirmed_models = []
while unconfirmed_models:
    currnet_model = unconfirmed_models.pop()
    print(f"Veryfiying model: {currnet_model.title()}")
    confirmed_models.append(currnet_model)
print("\nThe following models have been confirmed: ")
for confirmed_model in confirmed_models:
    print(confirmed_model.title())
