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
    'bob':'paladin',
    'tess':'rouge',
    'jenn':'cleric',
    'ross':'warlock',
}
character = character_choices['tess'].title()
print(f"Tess is playing as a {character}.")

print("\n")

cnc_1 = {'x_position':0,'y_position':10,'speed':'medium'}
cnc_value = cnc_1.get('z_position','No position value assigned.') #the get command is trying to get the z_position, but if it doesn't exist it will say 'No position value assigned.'
print(cnc_value) 

