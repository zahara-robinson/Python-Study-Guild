# ------------ 💗⚖️ COMPARISON OPERATORS ----------------   
# ----------------------------------------------------------------------
# Comparison operators are used to compare two values.
# They return a boolean value: True or False.

# Common comparison operators in Python:
#   ==  : Equal to
#   !=  : Not equal to
#   >   : Greater than
#   <   : Less than
#   >=  : Greater than or equal to
#   <=  : Less than or equal to
# ----------------------------------------------------------------------

# Example 1: Using '=='
x = 5
y = 5
print(x == y)  # Outputs: True (because 5 is equal to 5)

# Example 2: not equal to '!='
a = 10
b = 20
print(a != b)  # Outputs: True (because 10 is not equal to 20)

# Example 3: Greater than '>'
age = 18
print(age > 16)  # Outputs: True (because 18 is greater than 16)

# Example 4: Less than '<'
temperature = 60
print(temperature < 75)  # Outputs: True (because 60 is less than 75)

# Example 5: Greater than or equal to '>='
score = 90
print(score >= 90)  # Outputs: True (because 90 is equal to 90)

# Example 6: Less than or equal to '<='
money = 50
print(money <= 100)  # Outputs: True (because 50 is less than 100)

# Common mistake to avoid:
# if x = 5: wrong > this assigns 5 to x instead of comparing
# if x == 5: correct > this compares x to 5

# print("5" == 5) wrong types (string vs integer) > Outputs: False
print("5" == "5")  # correct types (string vs string) > Outputs: True


# ---------------------------------------------------------------
# Mini project: Grade Evaluator
# Concept: This program evaluates if a student has passed based on their score.

score = int(input("Enter your test score: "))

if score >= 90:
    print("You received an A. Excellent work!")
elif score >= 80:
    print("You received a B. Great job!")
elif score >= 70:
    print("You received a C. Good effort!")
elif score >= 60:
    print("You received a D. You passed, but there's room for improvement.")
else:
    print("You received an F. Unfortunately, you did not pass. Keep trying!")

# ---------------------------------------------------------------
# mini project: Temperature Comfort Checker
# Concept: Check if the temperature is within a comfortable range.

temperature = float(input("Enter the current temperature in Fahrenheit: "))

if temperature < 50:
    print("It's quite cold outside. Wear a warm jacket! 🧥")
elif temperature < 70:
    print("Mild and comfortable 🌤️.")
elif temperature < 90:
    print("It's getting warm. Stay hydrated! 💧")
else:
    print("It's very hot outside! Stay cool! 🥵")

# ---------------------------------------------------------------
# mini project: Cat Age comparison
# Concept: Compare the ages of two cats and determine which one is older. (using ==, >, < and etc.)

my_cat = int(input("Enter your cat's age in years: "))

if my_cat < 2:
    print("Your cat is a kitten! 🐱")
elif my_cat == 2:
    print("Your cat is a young adult cat! 🐱")
elif my_cat <= 7:
    print("Your cat is an adult cat! 🐱")
else:
    print("Your cat is a senior cat! 🐱")

# ---------------------------------------------------------------
# mini project: Password Strength Checker
# Concept: Check if a password is strong based on length and character variety.

password = input("Enter your password: ")
length = len(password)

print(f"\nPassword Length: {length} characters")

if length < 6:
    print("Password too weak! It should be at least 6 characters long.")
elif length >= 6 and length < 10:
    print("Password strength: Moderate. Consider adding more characters or symbols.")
elif length >= 10 and length < 14:
    print("Password strength: Strong!")
else:
    print("password strength: Very Strong!")