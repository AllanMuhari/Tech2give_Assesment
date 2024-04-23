# Question 2: Fibonacci Sequence
# Write a program to generate the Fibonacci sequence up to 100.

#solution 

def fibonacci_sequence():
    a, b = 0, 1
    while a < 100:
        print(a)
        a, b = b, a + b

fibonacci_sequence()