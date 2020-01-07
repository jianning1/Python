# Exercise 4: Variables and Names

cars = 100 # Total number of cars
space_in_a_car = 4.0 # How many people can seat in a car
drivers = 30 # Total number of drivers
passengers = 90 # Total number of passengers
cars_not_driven = cars - drivers # Total number of empty cars
cars_driven = drivers # Total number of cars on the road
carpool_capacity = cars_driven * space_in_a_car # Total spaces in cars on the road
average_passengers_per_car = passengers / cars_driven
# Average number of passengers each car need to carry

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
