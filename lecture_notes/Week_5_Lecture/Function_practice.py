def making_point():
    """This is a docstring describing what the function does"""
    print('function seems to work')

making_point()
making_point()
making_point()

def space():
    """Used to add a space inbetween each line"""
    print("\n")

space()

def greet_persons(person):
    """Dislay a simple greeeting to a user"""
    print(f"Hello, {person.title()}!")

greet_persons('mark')
greet_persons('mike')
greet_persons('susan')

space()

def machine_description(machine_type, axis):
    """Display a description of a machine"""
    print(f"\nI have a {machine_type}")
    print(f"The {machine_type} has {axis} axis.")

machine_description('mill',4) 
machine_description('lathe',2)
machine_description(3,'mill') #This causes it to read it has a 3 has mill axis

machine_description(machine_type='mill',axis=4)
machine_description(machine_type='lathe',axis=2)
machine_description(axis=3,machine_type='mill') #This makes it so the the order that I send it in doesn't matter 

def machine_description(axis, machine_type='mill'):
    """Display a description of a machine"""
    print(f"\nI have a {machine_type}.")
    print(f"The {machine_type} has {axis} axis.")

machine_description(axis=4) 
machine_description(machine_type='lathe',axis=2)

space()

def get_formatted_statement(application, technology):
    """Return a neatly formatted statement"""
    statment_full = f"{technology.upper()} {application.title()}"
    return statment_full

course_description = get_formatted_statement('programming','plc')
print(course_description)

space()

def build_couse(tech,app,credits=None):
    """Returea dictionary of a course description"""
    course = {'technolgy':tech, 'appliction':app}
    if credits:
        course['credits'] = credits 
    return course 

course_description = build_couse('plc','programming',credits=5)
print(course_description)