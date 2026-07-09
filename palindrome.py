# Approach 1: Basic

num = input("Enter a string: ")

rev_num = num[::-1]

if rev_num == num:
    print("Palindrome")
else:
    print("Not a palindrome")


# Approach 2: Optimized (ignore spaces & case)

s = input("Enter a string: ")

cleaned = s.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
