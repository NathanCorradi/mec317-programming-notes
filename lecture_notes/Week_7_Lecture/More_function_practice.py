def build_course(tech,app,credits = None):
    """ Return a dicticonary o fa course description"""
    course = {'technology':tech, 'application':app}
    if credits:
        course['credits'] = credits 
    return course 

def space():
    """put a space inbetween lines"""
    print("\n")

course_description = build_course('plc','programming',credits=5)
print(course_description)

space()

squawk = input("Type in what you would like repeated back to you: ")
print(squawk)

space()

name = input("please enter your name: ")
print(f"Hello, {name}!")

space()

prompt = "If you tell me who you are, I will personalize the message that you see."
prompt += "\nWhat is your first name? " #"+=" is used to add a line to the variable 
name = input(prompt)
print(f"Hello, {name}!") 

space()

plc_output = input("How many digital outputs does your PLC have? ")
plc_output = int(plc_output)
print(f"Your PLC has {plc_output} digital outputs! ")

space()

speed = input("What is your spindle speed in RPM? ")
speed = int(speed)

if speed >= 1800:
    print("\nSpindle speed too high for manual machining.")
else:
    print("\nSpindle speed suitable for manual machining.")

space()

number = input("Enter a number, I will check if it is an odd or even number!: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")


