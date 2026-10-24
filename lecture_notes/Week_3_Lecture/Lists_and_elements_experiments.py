#strings in a ([]) are a sign of a list
carbrands = ['volov','tesla','ford','toyota']
print(carbrands)

print(carbrands[0].title())
#having a number in ([]) will print one of the items in the list in order, remember that 0 is the starting number not 1
#you can also add things like title to uppercase the first letter in the word
#if you do a negative nummber you can go backwards in the list


carbrands = ['volov','tesla','ford','toyota','lada']
car_order = f"My next car will be a {carbrands[4].title()}"#change the presentation for print
print(car_order)

colors = ['red','green','yellow','purple']
print(colors)
colors[0] = 'brown' #used to replace red in the list with brown
print(colors) 
colors.append('pink') #used to add the color pink to the end of the list
print(colors)

colors = []
colors.append('megents')
colors.append('ham')
colors.append('pink')
print(colors)
#here I started with an empty list and added the differen't colors using the append command

colors = ['brown','red','purple']
print(colors)
colors.insert(0,'blue') #used to insert the color blue in the first spot of the list
print(colors)
del colors[2] #used to delete red from the list 
print(colors)

colors = ['brown','red','purple','blue']
print(colors)
popped_colors = colors.pop(1) 
#if left empty it pops the last color into its own variable, if you do this again it would just replace the previous color with the next one. 
#but if there is a number is the pop() command then it will take that nummber color 
print(colors)
print(popped_colors)

belt_colors = ['white','blue','purple','brown','black']
last_bjjbelt = belt_colors.pop() #used to pop the last color into "last_bjjbelt" 
print(f"The last belt on a BJJ journey is a {last_bjjbelt.title()} belt") #using the variable "last_bjjbelt" and capitalizing the first letter
belt_promotion = belt_colors.pop(2) #used to pop the third color into "belt_promotion" 
print(f"I got promoted to {belt_promotion.title()} belt today!") #using the variable "belt_promotion" and capitalizing the first letter

belt_colors = ['white','blue','purple','brown','black']
print(belt_colors)
belt_colors.remove('blue') #used to just remove the color blue from the list without having to know the number assoiated with it
print(belt_colors)

belt_colors = ['white','blue','purple','brown','black']
current_rank = 'purple'
belt_colors.remove(current_rank) #used to remove purple from "belt_colors" useing a variablem instead of just saying remove purple
#remove jsut removes the first purple it see's, if your list has more than one it won't remove all of the purples
print(belt_colors)
print(f"\nI currently hold the rank of {current_rank.title()} belt in BBJ") #"\n" is used here to start a new line

callsigns = ['charlie','alpha','delta','bravo']
callsigns.sort() #used to sort the list in an alphabetical order
#The sort command can't be reversed unless you remove it
print(callsigns)

callsigns = ['charlie','alpha','delta','bravo']
callsigns.sort(reverse=True) #used to sort the list in reverse alphabetical order
print(callsigns)

callsigns = ['charlie','alpha','delta','bravo']
print("here is the original list: ")
print(callsigns)
print("\nHere is the sorted list: ") #"\n" is used here to start a new line
print(sorted(callsigns)) #used to not permanently alter the list
print("\nHere is the original list again: ") #"\n" is used here to start a new line
print(callsigns)

callsigns = ['charlie','alpha','delta','bravo']
print("here is the original list: ")
print(callsigns)
print("\nHere is the sorted list: ") #"\n" is used here to start a new line
callsigns.sort() #used to permanently alter the list
print(callsigns) 
print("\nHere is the original list again: ") #"\n" is used here to start a new line
print(callsigns)

callsigns = ['charlie','alpha','delta','bravo']
print(callsigns)
callsigns.reverse() #used to just reverse the list
print(callsigns)
callsigns.reverse() #used to bring the list back to its original 
print(callsigns)

callsigns = ['charlie','alpha','delta','bravo']
length_callsign = len(callsigns) #used to see how many items are in the list
print(length_callsign)

