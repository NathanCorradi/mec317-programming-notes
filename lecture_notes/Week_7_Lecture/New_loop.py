def space():
    """used to add a space inbetween lines in the code"""
    print('\n')

current_number = 1
while current_number <=5: # while is a a loop that is active if the prompt is achived 
    print(current_number)
    current_number += 1 

space()

squawk = "\nTell me something, and I will repeat it to you:"
squawk += "\nEnter 'quit' to end the program. \n" # The "+=" is used to add a line to the variable
message = ""
while message != 'quit':
    message = input(squawk)
    print("\n")
    print(message)

