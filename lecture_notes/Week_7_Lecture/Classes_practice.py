class Machine:
    """Simple attempt to model a machine"""
    def __init__(self,type,voltage):
        """Initialize name and voltage atributes"""
        self.type = type
        self.voltage = voltage
    def cut(self):
        """Simulate a machine cutting in response to command"""
        print(f"{self.type} is now cutting the mtrl.")
    def thread(self):
        """simulate threading a mtrl in response to command"""
        print(f"{self.type} threaded the material.")

my_machine = Machine('lathe', 110) #assigned 'lathe' to type and '110' to voltage
nathan_machine = Machine('mill',230)
bob_machine = Machine('drillpress', 110)
mechlab_machine = Machine('mill', 220)

print(f"the machine is a {my_machine.type}.") #the .type calls out the assigned 'lathe'
print(f"The machine runs on {my_machine.voltage} volts") #the .voltage calls out the assigned '110'

my_machine.cut()
my_machine.thread()

print("\n")

print(f"I have a {my_machine.type.title()}.")
print(f"My {my_machine.type.title()} runs on {my_machine.voltage} Volts.")
my_machine.cut()

print(f"\nThe lab has a {mechlab_machine.voltage} Volt {mechlab_machine.type.title()}.")
mechlab_machine.thread()