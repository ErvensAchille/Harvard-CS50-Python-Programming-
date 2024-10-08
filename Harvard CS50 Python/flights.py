# This line defines a new class called Flight. A class is like a blueprint for creating objects
class Flight():
# This is the constructor method, which is called when a new object (instance) of the class is created. 
# The capacity parameter is passed when a Flight object is created, and it tells the program how 
# many passengers the flight can hold.
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
# This defines a method named addPassenger. It takes two arguments: self 
# (which refers to the current Flight object) and name, which is the name of the passenger.
# self.openSeats() calls another method openSeats to check if there are any open seats on the flight.
# if not self.openSeats() checks if there are no open seats left. If this is true, t
# he function returns False, meaning the passenger could not be added.
# If there are open seats, the passenger's name is added to the passengers list using the append() method.
    def addPassenger(self, name):
        if not self.openSeats():
            return False
        self.passengers.append(name)
        return True
# This defines another method, openSeats, which checks how many seats are still available.
# This calculates the number of open seats by subtracting the number of passengers already 
# on the flight (len(self.passengers)) from the total capacity of the flight (self.capacity).
    def openSeats(self):
        return self.capacity - len(self.passengers)

# Flight object        
flight = Flight(5)

people = ["Harry", "Ron", "Hermione", "Ginny"]

# This is a for loop that iterates over each person in the people list:

# flight.addPassenger(person) tries to add each person to the flight.
# If it succeeds (success is True), it prints a message saying the person was added to the flight.
# If it fails (success is False), it prints a message saying there were no seats left for that person.

for person in people:
    success = flight.addPassenger(person)
    if success:
        print(f"added {person} to flight")
    else: print (f"no seats for {person}")

# How the Code Runs:
# A flight with a capacity of 5 seats is created.
# The program attempts to add each person from the people list to the flight.
# For each person, it checks if there are enough open seats.
# If there are open seats, the passenger is added, and a success message is printed.
# If there are no seats left, a failure message is printed.
# In this case, the flight has enough capacity for all four people, so the program will add all of them successfully.