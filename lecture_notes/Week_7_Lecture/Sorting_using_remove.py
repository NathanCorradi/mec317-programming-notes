devices = ['siemes','ab','omron','ab','mitsubishi','click','siemens','ab']
print(devices)
while 'ab' in devices:
    devices.remove('ab')
print(devices)

print("\n")

responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("\nWhich class are you currently taking? ")
    responses[name] = response
    repeat = input("\nWould you like to let another person input data? (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} is currently taking {response}.")
dontstop = input("\n\nPress any Enter to continue... ")