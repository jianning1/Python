# Exercise 19 Functions and Variables

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")
# define cheese_and_crackers function, which has 2 Variables

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)
# use function cheese_and_crackers, cheese_count = 20, boxes_of_crackers = 30

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# input values by user
print("Please enter number of cheese you have:")
number_of_cheese = input()
print("Please enter number of crackers boxes you have:")
number_of_crackers_boxes = input()
cheese_and_crackers(number_of_cheese, number_of_crackers_boxes)
