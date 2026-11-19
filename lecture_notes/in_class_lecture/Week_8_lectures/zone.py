zones = [
    {"name": "Greenhouse", "temperature": 15, "min": 18, "max":26},
    {"name": "Storage Room", "temperature": 29, "min": 16, "max":24},
    {"name": "Workshop", "temperature": 21, "min": 19, "max":23},
]

def analyze_zone(current_temperature, min, max):
        heater_on = False
        fan_on = False
        if current_temperature < min:
            heater_on = True
        elif current_temperature < max:
           fan_on = True
        return heater_on, fan_on