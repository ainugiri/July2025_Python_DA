# Function definition / declaration
def greet_user(name = "Guest"):
    print(f"Hello, {name}! Welcome to Python Basics.")

# Function call
greet_user()
greet_user()

username = "Giri Prasad P"
greet_user(username)
greet_user("John Doe")
greet_user()


def add_numbers(a, b):
    """This function adds two numbers and returns the result."""
    return a + b

# lambda function
add = lambda a,b : a + b
# lambda function is a small anonymous function that can take any number of arguments but can only have one expression.
# if only one expression is there, we can use lambda function instead of defining a function using def keyword.

print(add_numbers(10, 20))  # Output: 30
print(add(10, 20))  # Output: 30
greet = lambda name="Guest": print(f"Hello, {name}! Welcome to Python Basics.")
greet()
greet("Alice")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Make: {self.make}, Model: {self.model}, Year: {self.year}")
def main():
    # Create an instance of the Car class
    my_car = Car("Toyota", "Corolla", 2020)
    
    # Call the display_info method
    my_car.display_info()