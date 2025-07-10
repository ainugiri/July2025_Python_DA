# class is blueprint for creating objects
# set of properties and methods
# for initializing the properties, we use __init__ method
# __init__ method is called when an object is created from a class
# constructor method __init_ is used to initialize the properties of the class

# for car class -> properties are make, model, year, fueltype
# functions -> start, stop, accelerate, brake, display_info
# self is a reference to the current instance of the class
# it is used to access the properties and methods of the class
class Car:
    def __init__(self, make, model, year, fueltype):
        self.make = make
        self.model = model
        self.year = year
        self.fueltype = fueltype

    def start(self):
        print(f"{self.make} {self.model} is starting.")

    def stop(self):
        print(f"{self.make} {self.model} is stopping.")

    def accelerate(self):
        print(f"{self.make} {self.model} is accelerating.")

    def brake(self):
        print(f"{self.make} {self.model} is braking.")

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}, Fuel Type: {self.fueltype}")

def main():
    # Create an instance of the Car class
    my_car = Car("Toyota", "Corolla", 2020, "Petrol")
    
    # Call the methods
    my_car.start()
    my_car.accelerate()
    my_car.brake()
    my_car.stop()
    
    # Display car information
    my_car.display_info()

    c2 = Car("Honda", "Civic", 2021, "Diesel")
    c2.start()
    c2.accelerate()
    c2.brake()

    c3 = Car("Ford", "Mustang", 2022, "Electric")
    c3.start()
    c3.accelerate()
    c3.brake()
    c3.stop()
    c3.display_info()
