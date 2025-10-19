# ------------------ 💜 Conditional Statements - if, else, elif 💜 ---------------------
# if - Checks a condition, if that condition is True it runs the code under it. If It's False, it simply skips it and moves on.
# Should be
age = 18
if age >= 18:
    print("You can vote!")

is_logged_in = True
if is_logged_in:
    print("You are logged in!")

name = "Zunnie"
if name == "Zunnie":
    print("Hello, Queen!") # Uses == to compare values (not = which assigns).

temperature = 90
if temperature > 79:
    print("Its nice today!") # Works with numbers, booleans, and comparisons.

score = 0
if score == 0:
    score += 10
    print("bonus applied!", score) # Multiple lines under if — all indented equally.

# Should never....
# if 5 > 3
    print("True") # Missing colon (:) at the end of the if statement. Fix: if 5 > 3:
# if age = 18:
    print("Adult") # Used single = (assignment) instead of == (comparison).Fix: if age == 18:
# if true:
    print("Yes") # Missing indentation — Python doesn’t know what belongs inside the if.
# if "Zunnie":
    print("Hello") # Non-boolean condition — should be a comparison or boolean variable. Fix: if name == "Zunnie":
# if 10 > 5:
    print("Yes")
    print("Still inside")
print("Outside") # Last print is outside the if (not indented) so it always runs.
# if = "only if this is true, do the following": 1. always ends with : 2. code under it must be indented 3. use == to compare values and not = 4. can stand alone

# Elif - if this is true, do this, else if other thing is true, do that. otherwise (else) do something else.
# its the "middle check" between if and else
# if condition1:
    # code to run if condition1 is true
# elif condition2:
    # code to run if condition2 is true

#should be
age = 16
if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager") # Checks second condition only if the first fails.

score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C") # Multiple elif blocks can exist — Python checks them top to bottom until one is True.

    temperature = 60

if temperature > 80:
    print("Hot")
elif temperature > 50:
    print("Warm")
elif temperature > 30:
    print("Cool") # Only the first True condition runs, even if others could also be True.

day = "Saturday"

if day == "Friday":
    print("TGIF!")
elif day == "Saturday" or day == "Sunday":
    print("It's the weekend!") # Can use logical operators (and, or) in conditions.

num = 0

if num > 0:
    print("Positive")
elif num == 0:
    print("Zero") 

# Should never....
# elif x > 5: # Cant start without if before it
#    print("x is greater than 5") 
#fix:
# if x > 5:
#    print("huge")
# elif x > 10:
#    print("massive")

# if x > 5:
#    print("Yes")
# elif: 
#    print("No") # Missing condition after elif. Fix: elif x < 5:

# if score > 90:
    print("A")
# elif score > 80
    print("B") # Missing colon (:) at the end of the elif statement. Fix: elif score > 80:  

if age > 18:
    print("Adult")
elif age > 13:
    print("Teen") # Missing indentation — Python doesn’t know what belongs inside the elif. 

if num > 0:
    print("Positive")
elif num > 0:
    print("Also Positive") # Redundant condition — elif checks the same thing as if. Fix: use a different condition.

# else - if if and Elif conditions were false, do this.

# if:
    # code to run if condition is true
# else:
    # code to run if condition is false

# Should be
age = 16
if age >= 18:
    print("Adult")
else:
    print("Minor") # Runs when the if condition is False.

is_logged_in = False
if is_logged_in:
    print("Welcome back!")
else:
    print("Please log in.") # Simple if-else structure for two outcomes.

temperature = 40
if temperature > 79:
    print("Nice weather!")
else:
    print("Bring a jacket.") # Works with numbers, booleans, and comparisons.

grade = 85
if grade < 60:
    print("Failed")
elif grade < 90:
    print("Passed")
else:
    print("Excellent!") # Combines if, elif, and else for multiple branches.

has_pet = True
if has_pet:
    print("You must love animals!")
else:
    print("No pets? More freedom!") # Can use else after multiple elif checks.

# Should never....
# else:
#    print("Hi") you cant start with else. must have "if" before it

# if x > 4:
#  print("x is greater")
#else x < 4: <- else cant have a condition after it
#  print("x is smaller")
#fix:
# if x > 4:
#    print("x is greater")
# else:
#    print("x is smaller")

# if True:
#  print("Yes") 
# else
#  print ("Nope") # Missing colon (:) at the end of the else statement. Fix: else:

# if age >= 18:
#    print("Adult")
# else:
#print("Minor") # Missing indentation — Python doesn’t know what belongs inside the else.
#fix:
if age >= 18:
    print("Adult")
else:
    print("Minor")

# if temperature > 80:
#    print("Hot")
# else:
#    print("Hot") Both say the same thing — pointless use of else. Fix: change the else message to something different.

# else takes no condition. it runs when all previous if and elif conditions were false.

# Combined Example
# Should be:
#1. Order from most specific → least specific
score = 93
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    grade = "C or below" 

# 2. Use non-overlapping ranges
temp = 66
if temp < 32:
    state = "Freezing"
elif 32 <= temp <= 69:
    state = "Cold"
else:
    state = "Warm"

# 3. Keep conditions readable
is_member = True
cart_total = 80
if is_member and cart_total >= 50:
    discount = 0.15
elif cart_total >= 100:
    discount = 0.10
else:
    discount = 0.00

# 4. Use elif instead of nested if chains when choices are exclusive
day = "Sat"
if day in ("Sat", "Sun"):
    activity = "Relax"
elif day == "Fri":
    activity = "Party"
else:
    activity = "Work"

# 5. Have a meaningful else as a fallback
file_type = ".png"
if file_type == ".jpg":
    process = "Process JPEG"
elif file_type == ".png":
    process = "Process PNG"
else:
    process = "Unsupported format"

# should never.... (commoon mistakes)
# 1. Don’t put overlapping conditions in the wrong order
# age = 20 
# if age >= 18: # first condition the later ">=21" from ever hitting for 21+
#    label = "Adult"
# elif age >= 21:
#    label = "21+"

# 2. Don’t repeat the same condition
# n = 5
# if n > 0:
#    result = "Positive"
# elif n > 0: # repeated condition. wont run
#    result = "Also Positive"

# 3. Don’t use else when you mean another elif
# color = "blue"
# if color == "red":
#    tag = 1
# else:
#    tag = 2 # blue/ other colors all get tag 2 by accident
#fix:
color = "blue"
if color == "red":
    tag = 1
elif color == "blue":
    tag = 2
else:
    tag = 3

# 4. Don’t mix incomparable types
# age = "18" # string
# if age > 17: # comparing string to int will cause error
#    ...

# 5. Don’t forget the colon or indentation
# if ready
# print("Go!") # missing colon and indentation
# if ready:
# print("Go!") # missing indentation

# Real-life coder examples
# 1) Login & role-based greeting
is_logged_in = True
role = "Moderator" # Admin, User, Guest

if not is_logged_in:
    print("Please log in.")
elif role == "Admin":
    print("Welcome back, Admin!")
elif role == "Moderator":
    print("Hello, Moderator! limited access granted.")
else:
    print("Welcome, User! Enjoy your stay.") # Use case: dashboards, permission gates.

# 2) Shipping cost calculator
cart_total = 120.00
destination = "International" # Domestic, International

if cart_total >= 100:
    shipping_cost = 0.00
elif destination == "international":
    shipping_cost = 25.00
else:
    shipping_cost = 5.00 # Use case: e-commerce checkout systems.
print(f"Your shipping cost is: ${shipping_cost}")

# doing it myself
#a. if + Else
n = -2 #change this value to test
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

# b) If + Elif (multi-choice, no final else)
month = 7 #change this value to test
if month in (12, 1, 2):
    print("Winter")
elif month in (3, 4, 5):
    print("Spring")
elif month in (6, 7, 8):
    print("Summer")
elif month in (9, 10, 11):
    print("Fall")

# C) if + Elif + Else (full chain with safe fallback)
score = 58 #change this value to test
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
elif 0 <= score < 60:
    print("F")
else:
    print("Invalid score")