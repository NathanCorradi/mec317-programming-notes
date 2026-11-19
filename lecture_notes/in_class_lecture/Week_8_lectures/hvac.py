"""
Create a program that manages a multizone hvac system
(1) Good functions "do 1 thing
    [verb]_[what the verb is acting on]
    Ex: def calculate_stud_dimensions()

(2) No repeated code
"""

zones = [
    {"name": "Greenhouse", "temperature": 15, "min": 18, "max":26},
    {"name": "Storage Room", "temperature": 29, "min": 16, "max":24},
    {"name": "Workshop", "temperature": 21, "min": 19, "max":23},
]

def adjust_hvac_rooms(name, temp, min, max):
    """looks at the different temp in different rooms,
    and prints a """
    print(f"The {name} temperature is {temp}.")
    if temp < min:
        print(f"It is too cold in {name} turning up the heater now.")
    elif temp > max:
        print(f"It is too hot in {name} turning on the fan now.")
    else:
        print(f"The temperature in {name} is fine.")

for room in zones:
    if zones[0] in zones:
        adjust_hvac_rooms(zones[0]['name'],zones[0]['temperature'],zones[0]['min'],zones[0]['max'])

print("\n")

adjust_hvac_rooms(zones[0]['name'],zones[0]['temperature'],zones[0]['min'],zones[0]['max'])

print("\n")

#Greenhouse 
zone = zones[0]

if zone ["temperature"] < zone["min"]:
    print("Heater on")
    print("Fan off")
elif zone["temperature"] < zone["max"]:
    print("Heater off")
    print("Fan on")
else:
    print("Heater off")
    print("Fan off")

#Storage Room
zone = zones[1]

if zone ["temperature"] < zone["min"]:
    print("Heater on")
    print("Fan off")
elif zone["temperature"] < zone["max"]:
    print("Heater off")
    print("Fan on")
else:
    print("Heater off")
    print("Fan off")

#Workshop
zone = zones[2]

if zone ["temperature"] < zone["min"]:
    print("Heater on")
    print("Fan off")
elif zone["temperature"] < zone["max"]:
    print("Heater off")
    print("Fan on")
else:
    print("Heater off")
    print("Fan off")

