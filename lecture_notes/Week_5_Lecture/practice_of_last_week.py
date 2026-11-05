for value in range(1,6): #range you just give a range of numbers to go though, if you don't give a starting number then it starts at 0
    print(value)

print("\n")

numbers = list(range(1,6)) #the list command is just an easier way to make a list
yet_numbers = []
print(numbers)
print(yet_numbers)

print("\n")

even_numbers = list(range(2,11,2)) #this range went through 2 to 11 by increments of 2 
print(even_numbers)

print("\n")

power_up = []
for value in range(1,11): #run a for loop for 10 iterations 
    power_to = value **2 #take the currents interation number of the for loop and square it
    power_up.append(power_to) #add the squared loop iteration number to our list power_up
print(power_up)

print("\n")

numbers_range = [1,2,3,4,5,6,7,8,9,0]
work = min(numbers_range) #gives the smallest number in the list
print(work)
work = max(numbers_range) #gives the largest number in the list
print(work)
work = sum(numbers_range) #gives the sum of all the numbers in the list
print(work)

print("\n")

power_up2 = [value**2 for value in range (1,11)] #this line of code is used to complete the same process has the first power_up in way shorter space
print(power_up2)

print("\n")

colors = ['red','blue','green','purple','brown','black']
print(colors[0:4]) #how you chose what parts of your list you want printed 

print("\n")

colors = ['red','blue','green','purple','purple','brown','black']
print("here are the first three colors of the list: ")
for color in colors[:3]:
    print(color.title())

print("\n")

pizza_toppings = ['cheese','salami','pepperoni','onion','garlic']
pizza_order = pizza_toppings[:] # this is how to pick what toppings you want on the pizza_order
pizza_toppings.append('ham') #this is adding to the topping selection
pizza_order.append('strawerry') #this is adding to the pizza_order without having it in the pizza_toppings list
print("These are our toppings: ")
print(pizza_toppings)
print("\nCustomer ordered: ")
print(pizza_order)

print("\n")

pizza_toppings = ['cheese','salami','pepperoni','onion','garlic']
pizza_order = pizza_toppings #Without the [:] it is saying the pizza_toppings and pizza_orders are the same always. with the [:] it just copies the list at that time
pizza_order.append('ham')
pizza_toppings.append('strawberry')
print("This are our toppings: ")
print(pizza_toppings)
print("\nThe Custormer ordered: ")
print(pizza_order)

print("\n")

#tuple list are lists that don't change 
triange_sides = (200,50,150)
print(triange_sides[0])
print(triange_sides[1])

print("\n")

my_tuple = ('red','brown',2,'orange')
print(my_tuple)

print("\n")

triange_sides = (200,50,155)
for side in triange_sides:
    print(side)

triange_sides = (400,100,310) #you can't change tuples but you can overwrite them
print("\nChanged dimensions: ")
for side in triange_sides:
    print(side)

print("\n")

pizza_toppings = ['cheese','salami','pepperoni','onion','garlic']
if 'cheese' in pizza_toppings: #the in is checking if 'cheese' is in the pizza_toppings list
    print("that works!") #if cheese is in the list it will then print "that works!" 
if 'onion'not in pizza_toppings: #the not in is checking if 'onion' isn't in the pizza_toppings list
    print("invalid topping") #if onion wasn't in the list it would print "invalid topping"

print("\n")

requested_features = ['all wheel drive','manual transmission']
if 'two wheel drvie' in requested_features: 
    print("adding two wheel drive")
if 'all wheel drive' in requested_features:
    print("adding all wheel drive")
if 'automatic transmission' in requested_features:
    print("adding automatic transmission")
if 'manual transmission' in requested_features:
    print("adding manual transmission")
print("\nProcessing your final vehicle order!")

print("\n")

available_features = ["keyboard",'mouse','processor','ram','monitor','speakers']
requested_features = ['keyboard','mouse','track pad',]
for requested_feature in requested_features: 
    if requested_feature in available_features: #this is checking if the requested_feature is in the available_feactures
        print(f"Adding {requested_feature.title()}.") #if the feature is in the list it will print a messages saying that it is adding it. 
    else:
        print(f"Sorry, we don't have a {requested_feature}")
print("\nFinished processing your order!")
