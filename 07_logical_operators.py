# ------------------💻💖 Logical Operators ------------------
# Logical operators: and, or, not.
# Connect multiple conditions in an if statement.
# They return a boolean value: True or False.
# ----------------------------------------------------------------------

# and: all conditions must be True. 
# Example 1: Using 'and'
x = 8
print(x > 5 and x < 10)  # Outputs: True (because both conditions are True)

# or: at least one condition must be True.
# Example 2: Using 'or'
x = 12
print(x > 10 or x < 5)  # Outputs: True (because the first condition is True)

# not: reverses the boolean value.
# Example 3: Using 'not'
is_raining = False
print(not is_raining)  # Outputs: True (because not False is True)

# Combined Example:
age = 25
has_id = True
if age >= 18 and has_id:
    print("You are allowed to enter the club.")
else:
    print("You are not allowed to enter the club.")

# using or for flexibility
pet = "Cat"
if pet == "dog" or pet == "cat":
    print("You have a common pet.")

# ---------------------------------------------------------------

# Should not be examples:

# 1. 
# x = 10
# if x > 5 and: # missing second condition
#     print("yes")

# 2.
# if True or False and False: # misunderstanding order - and runs before or
#     print("This is confusing without parentheses")
# Correct way with parentheses:
if (True or False) and False:
    print("This is clearer with parentheses")

# 3.
# if not True == False: # Harder to read
#    print("Huh?")
# Better way:
if not (True == False):
    print("Much clearer!")

# 4.
# if not x > 5 and y < 10: # confusing precedence - not applies only x > 5
# fix: add parentheses

# 5.
# if age > 18 or age < 30: # cant leave comparison open
# fix: 
# if age > 18 or age <30:

# ---------------------------------------------------------------

# More expamples:

# 1. Club Entry system
age = int(input("Enter your age: "))
has_id = input ("Do you have ID? (yes/no): ")

if age >= 18 and has_id.lower() == "yes":
    print("You can enter the club.")
else:
    print("You cannot enter the club.")

# 2. discount eligibility
total = float(input("Enter total purchase amount: "))
memeber = input("Are you a member? (yes/no): ")

if total > 100 or memeber == "yes":
    print("You are eligible for a discount!")
else:
    print("You are not eligible for a discount.")

# 3. Weather Decision
is_raining = True
is_cold = True

if is_raining and is_cold:
    print("Wear a raincoat and a sweater.")
elif is_raining or is_cold:
    print("Carry an umbrella or wear a sweater.")
else:
    print("It's a nice day!")

# ---------------------------------------------------------------

# Practice Problems:

# A. Movie Eligibility
age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age >= 13 and has_ticket.lower() == "yes":
    print("Enjoy the movie")
else:
    print("Not allowed")

# b. Weekend Reminder
day = input("Enter day: ")

if day == "satuday" or day == "Sunday":
    print("Time to relax!")
else: 
    print("Keep on grinding!")
