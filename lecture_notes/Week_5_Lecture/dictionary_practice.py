vehicle_0 = {'color':'blue','wheels':4} #a dictionary is a a list of key pairs, an example is color = blue now 
drive_info = vehicle_0['wheels']
print(f"You are utilizing {drive_info} wheel drive")
print(vehicle_0)
vehicle_0['x_coordinate'] = 15 #this is adding a new key pair to the dictionary
vehicle_0['y_coordinate'] = 55 #you can also had strings, it doesn't just have to be numbers
print(vehicle_0)

print("\n")

vehicle_0 = {}
vehicle_0['color'] = 'blue'
vehicle_0['wheels'] = 4
print(vehicle_0)
print(f"The car is {vehicle_0['color']}.")
vehicle_0['color'] = 'red' #this is to overwrite the blue color to red
print(f"The car is now {vehicle_0['color']}.")

print("\n")

cnc_1 = {'x_position':0,'y_position':10,'speed':'medium'}
print(f"Original Machine position: {cnc_1['x_position']},{cnc_1['y_position']}")
if cnc_1['speed'] =='slow': #checking to see if the speed is 'slow', 'mediume', or something else 
    x_increment = 1
elif cnc_1['speed'] =='medium':
    x_increment = 2
else:
    x_increment = 3
cnc_1['x_position'] = cnc_1['x_position'] + x_increment #it then will take the x_position and add based on what the speed is 
print(f"New Machine position: {cnc_1['x_position']},{cnc_1['y_position']}")

print("\n")

print(cnc_1)
del cnc_1['speed']
print(cnc_1)

print("\n")

character_choices = { #this is a way to lay out the dictionary that looks better for humans 
    'bob':['paladin'],
    'tess':['rouge'],
    'jenn':['cleric'],
    'ross':['warlock'],
    'mike':['paladin'],
}
character = character_choices['tess']
print(f"Tess is playing as a {character}.")

print("\n")

cnc_1 = {'x_position':0,'y_position':10,'speed':'medium'}
cnc_value = cnc_1.get('z_position','No position value assigned.') #the get command is trying to get the z_position, but if it doesn't exist it will say 'No position value assigned.'
print(cnc_value) 

for name,class_type in character_choices.items(): #.items() allows there to be to items in the selection in the for loop
    #print(f"\nName of Attendee: {name.title()}")
    #print(f"Class Type: {class_type.title()}")
    print(f"\n{name.title()} is playing as a {class_type}")

print("\n")

for name in character_choices.keys(): #used to just grab the keys in the dictionary, the default is just keys
    print(f"Hi {name.title()}.")

print("\n")

for class_type in character_choices.values(): #used to just grab the value in the dictionary
    print(F"{class_type} is a playable class.")

print("\n")

for name in character_choices: #used to show that the default is keys
    print(f"Hi {name.title()}.")

print("\n")

if 'mike' not in character_choices.keys():
    print("Mike, Pick a class!")

print("\n")

for name in sorted(character_choices.keys()): #used to sort the dictionary while grabing the keys
    print(f"{name.title()} thank you for attending this session.")

print("\n")

#for unique_classes in set(character_choices.values()): #used to just grab the unique values out of the dictionary 
 #   print(unique_classes)

print("\n")

for name, char_classes in character_choices.items():
    print(f"\n{name.title()} is playing as a: ")
    for char_class in char_classes: #for loop inside of a for loop using the previous local variable 
        print(f"\t{char_class.title()}") #\t is used to tab 


print("\n")


cnc_0 = {'type':'mill','axis':3,'power':'220 Volt'}
cnc_1 = {'type':'lathe','axis':2,'power':'120 Volt'}
cnc_2 = {'type':'mill','axis':5,'power':'480 Volt'}

cncs = [cnc_0,cnc_1,cnc_2]

for cnc in cncs:
    print(cnc) 

print("\n")

machine_operators = {
    'bross':{
        'first':'bob',
        'last':'ross',
        'shift':'first',
    },
    'mrogers':{
        'first':'mr',
        'last':'rogers',
        'shift':'night',
    },
}
for username, operator_info in machine_operators.items(): #username is the key in the first dictionary, operator_info is the value in the first dictionary 
    print(f"\nUsername: {username}")
    full_name = f"{operator_info['first']} {operator_info['last']}" #used to grab values from the second dictionary 
    shift = operator_info['shift']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tShift: {shift.title()}")

