class Car:
    """Representign commonalities about cars"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe cars"""
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

my_car = Car('toyota','hilux','2010')
print(my_car.get_descriptive_name())

