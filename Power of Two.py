# Question 3: Power of Two
# Write a program that takes an integer as input and returns true if the input is a power of two.

def power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

print(power_of_two(16)) # True
print(power_of_two(18)) # False