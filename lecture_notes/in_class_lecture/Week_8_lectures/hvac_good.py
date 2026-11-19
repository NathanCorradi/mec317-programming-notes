"""
what makes this approach good?

- reduce repeated code
- use the zones list to our advantage
- going to be shorter

What is bad about this approach?

- the functuion is relying on a certain shape to the dictionary
- the fuction prints instead of returns called a "side effect"
"""

zones = [
    {"name": "Greenhouse", "temperature": 15, "min": 18, "max":26},
    {"name": "Storage Room", "temperature": 29, "min": 16, "max":24},
    {"name": "Workshop", "temperature": 21, "min": 19, "max":23},
]

def analyze_zone(zone):
    if zone ["temperature"] < zone["min"]:
        print("Heater on")
        print("Fan off")
    elif zone["temperature"] < zone["max"]:
        print("Heater off")
        print("Fan on")
    else:
        print("Heater off")
        print("Fan off")


#look at every room in the property
for zone in zones:
    #analyze the temperature in each room
    analyze_zone(zone)

custom_zone = {
    "name":"Gym",
    "min":10,
    "max":20,
}

analyze_zone(custom_zone)