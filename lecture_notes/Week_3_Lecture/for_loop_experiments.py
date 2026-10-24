carbrands = ['bmw','volvo','tesla','volga']
for brand in carbrands: #used to make a local variable for each element that is than used in a for loop
    print(brand)

for x in range(4): #range is used to make a range used in a for loop 
    print(x)

for milkshake in range(7,13):
    print(milkshake)

print("\n") #used to seperate these sections apart

carbrands = ['bmw','volvo','tesla','volga']
for brand in carbrands:
    print(f"{brand.title()} made a beautiful car this year!") 
    print(f"I can't wait to see what {brand.title()} will produce next year!\n")
print("this is the line that will show the difference between loop and not in loop")
#This for loop is used to make the same messages for all car brands 

carbrands = ['bmw','volvo','tesla','volga','volvo']
for car in carbrands:
    if car == 'volvo': #used to find all the 'volvo's in the list and if it finds one it prints it, the (==) means equal to 
        print(car.title())

print("\n")

carbrands = ['bmw','volvo','tesla','volga','volvo',"gmc"]
for car in carbrands:
    if car == 'gmc' or car == 'bmw': #the or is used to add onto the if statment
        print(car.upper())
    else: #used to add on to the for loop for the car's that aren't labled in the if statment
        print(car.title())    

print("\n")

age = 3
if age < 4 or age == 4: #the or command is used to make an equal or less than sign
    print('Your fair admission cost is $5')
elif age < 18 or age == 18: #  elif is used to add another condition to the if statement 
    print('Your fair admission cost is $10')
elif age == 65 or age > 65:
    print('Your fair admission cost is $12')
else: #else is used to give an answer to any condition that wasn't labled in the if/elif statement 
    print('Your fair admission cost is $15')

print(f"age is {age}")