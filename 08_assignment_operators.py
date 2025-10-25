#--------💗🪞 Assignment Operators ----------
# Assignment operators are how we store or update values inside variables.
# They include: =, +=, -=, *=, /=, %=, **=, //=.
# ----------------------------------------------------------------------

# basic assignment
x = 5 # store 5 inside variable x

# add and assign +=
x = 5
x += 3 # same as x = x + 3
print(x) # Outputs: 8

# subtract and assign -=
x = 10
x -= 4 # same as x = x - 4
print(x) # Outputs: 6
# useful for countdowns, scores, or loop updates

# multiply and assign *=
z = 4
z *= 2 # same as z = z * 2
print(z) # Outputs: 8
# common in scaling values, like adjusting prices or distances

# divide and assign /=
a = 9
a /= 3 # same as a = a / 3
print(a) # Outputs: 3.0
# always results in a float, even if the division is exact

# floor divide and assign //=
b = 10
b //= 3 # same as b = b // 3
print(b) # Outputs: 3
# cuts off the decimal part, greater for integer division, useful for counting items or pagination

# modulus and assign %=
c = 10
c %= 4 # same as c = c % 4
print(c) # Outputs: 2
# give the remainder helpful for even/odd logic

# exponent and assign **=
n = 2
n **= 3 # same as n = n ** 3
print(n) # Outputs: 8
# perfect for powers or growth formulas

# --------------------------------------------------------

# bitwise operators and assign (not covered in this snippet but worth mentioning):

# bitwise AND and assign &=
d = 5  # in binary: 0101
d &= 3  # in binary: 0011
print(d)  # Outputs: 1 (in binary: 0001)

# bitwise OR and assign |=
e = 5  # in binary: 0101
e |= 3  # in binary: 0011
print(e)  # Outputs: 7 (in binary: 0111)

# bitwise XOR and assign ^=
f = 5  # in binary: 0101
f ^= 3  # in binary: 0011
print(f)  # Outputs: 6 (in binary: 0110)

# bitwise left shift and assign <<=
g = 1  # in binary: 0001
g <<= 2  # shift left by 2 (in binary: 0001 becomes 0100)
print(g)  # Outputs: 4 (in binary: 0100)

# bitwise right shift and assign >>=
h = 8  # in binary: 1000
h >>= 2  # shift right by 2 (in binary: 1000 becomes 0010)
print(h)  # Outputs: 2 (in binary: 0010)

# --------------------------------------------------------

# 5 Should be examples:
x = 10
x += 5  # x is now 15
x -= 2  # x is now 13
x *= 3  # x is now 39
x /= 3  # x is now 13.0
x **= 2  # x is now 169.0
x //= 4  # x is now 42.0
x %= 5  # x is now 2.0

# 5 should not be examples:
# 10 = x # cannot assign to a number, this will raise a SyntaxError
# x + = 5 # no space allowed between the operator, this will raise a SyntaxError
# x := 5 # assignment expression (walrus operator) is not valid in this context, it will raise a SyntaxError
# x =+ 5 # not the same as x += 5, this will assign +5 to x, which is just 5, not adding to the existing value of x
# x // = 2 # no space allowed between the operator, this will raise a SyntaxError

# --------------------------------------------------------
# More examples of assignment operators in use:

player_score = 0
player_score += 1 #player won a round
print("Score:", player_score) # Outputs: Score
# everytime the player wins, we can use += to update their score without needing to write player_score = player_score + 1 each time.

