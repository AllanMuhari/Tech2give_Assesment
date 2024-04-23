# Question 6: Count Vowels
# Write a program that counts the number of vowels in a sentence.

# eg " Hello World " => returns 2

def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiou":
            count += 1
    return count

print(count_vowels("Hello World")) # 3