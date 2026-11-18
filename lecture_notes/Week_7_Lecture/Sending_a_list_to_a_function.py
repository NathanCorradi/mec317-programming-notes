def greet_user(names):
    """print a simple greeting to each user in a list"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['bob','cindy','mark']
greet_user (usernames)

print("\n")

def machine_parts(wip_designs, completed_parts):
    """
    Simulate machining each part until none are left.
    Move each part to completed_parts after machining.
    """
    while wip_designs:
        current_part = wip_designs.pop()
        print(f"Machining parts: {current_part}")
        completed_parts.append(current_part)

def show_completed_parts(completed_part):
    """Show all the parts that were machined"""
    print("\nThe followig parts have been machined.")
    for completed_part in completed_parts:
        print(completed_part)

wip_designs = ['fixture plate','bracket','pulley','cog']
completed_parts = []
machine_parts(wip_designs, completed_parts)
show_completed_parts(completed_parts)
print(wip_designs)