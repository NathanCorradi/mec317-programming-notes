from zone import zones, analyze_zone

def main():
     #look at every room in the property
    for zone in zones:
        #analyze the temperature in each room
        zone_temp = zone["temperature"]
        zone_min = zone["min"]
        zone_max = zone["max"]
        heater_on, fan_on = analyze_zone(zone_temp,zone_min,zone_max)

        #output a report
        print("Checking", zone["name"], "...")
        print("Heater ON" if heater_on else "Heater OFF")
        print("Fan ON" if fan_on else "Fan OFF")

main()
