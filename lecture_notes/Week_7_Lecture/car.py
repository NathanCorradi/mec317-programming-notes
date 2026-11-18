class Car:
    """Representign commonalities about cars"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe cars"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def read_odometer(self):
        """A printed statement showing the cars milage"""
        print(f"This car has {self.odometer_reading} km on it.")
    def update_odometer(self, milage):
        """
        Set the odometer readign to a given value.
        Reject the cange if new is lower than the old.
        """
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("Rolling back the odometer is a felony!")
    def increment_odometer(self, km):
        """Add the given amout to the odometer reading"""
        self.odometer_reading += km 

class ElectricCar(Car):
    """Represents aspects of the class car and sepects of a car, 
    specific to eletric cars
    """
    def __init__(self,make,model,year):
        """Initalize attributes of the partent class"""
        super().__init__(make,model,year)
        self.battery = Battery()
    def describe_battery(self):
        """Print a statement describing battery size"""
        print(f"This car has a {self.battery} -kWh battery.")
    def gas_tank_size(self):
        """Electriv cars do not have a gas tank size"""
        print("This car does not ahve a gas tank") 

class Battery:
    """A model for the batteries of electrive cars"""
    def __init__(self,battery_size = 60):
        """Initialize the batteries attributes"""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the battery size"""
        print(f"This car has a {self.battery_size} -kWh battery.")       
    def get_range(self):
        """Print a statement about the range of the battery"""
        if self.battery_size == 60:
            distance = 260 
        elif self.battery_size == 100:
            distance = 315
        print(f"This car can go about {distance} km on a full charge.")




user_says = 99
my_car = Car('toyota','hilux','2010')
nathans_car = Car('volvo','760','1984')

print(my_car.get_descriptive_name())
my_car.read_odometer()

my_car.odometer_reading = 55
my_car.read_odometer()

nathans_car.odometer_reading = 80000000
nathans_car.read_odometer()

my_car.year = 2000
print(my_car.get_descriptive_name())

print("\n")

my_car.update_odometer(user_says)
my_car.read_odometer()
my_car.update_odometer(55)

print("\n")

my_new_car = Car('volvo','v70', 2015)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23_500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

print("\n")

my_electric = ElectricCar('nissan','leaf',2018)
print(my_electric.get_descriptive_name())
my_electric.battery.describe_battery()
my_electric.update_odometer(30_550)
my_electric.read_odometer()
my_electric.battery.get_range()