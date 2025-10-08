# Print the multiplication table of 2 (from 2 × 1 up to 2 × 10) using a for loop.
# start = 1
# end = 10
# while start <= end :
#     print(start*2)
#     start += 1

# Find the factorial of a number N using a for loop.
# N = int(input("Enter your number: "))
# fact = 1

# for i in range(1, N + 1):
#     fact *= i
# print(fact)

# Find the sum of all even numbers up to N using a for loop.
# N = int(input("Enter a number: "))
# total = 0

# for i in range(2, N + 1, 2):
#     total += i
# print(total)

# Print the sum for first N multiples of 5, if n = 3 then print 5 + 10 + 15 = 30
# N = int(input("Enter your number: "))
# total = 0

# for i in range(1, N + 1):
#     total += i * 5

# print("Sum =", total)

# Print a number n = 5 n number of times if n = 5 then print 5 5 5 5 5, if n = 3 print 3 3 3
# N = int(input("Enter your number: "))
# start = 1
# while start <= N :
#     print(N)
#     start += 1

# Print all the multiples of 2 between a and b
# a = int(input("Enter your number: "))
# b = int(input("Enter your number: "))
# while a <= b :
#     if a % 2 == 0 :
#         print(a)
#     a += 1

# Lily is N years old.
# On every odd birthday (1, 3, 5, …) → she gets 1 toy.
# On every even birthday (2, 4, 6, …) → she gets money.
# The money starts at ₹10 on her 2nd birthday.
# On each next even birthday, it increases by ₹10 more:
# 2nd birthday → ₹10
# 4th birthday → ₹20
# 6th birthday → ₹30
# and so on.
# At the end, print the following:
# * Number of toys Lily has.
# * Total money she has (money from even birthdays after brother takes ₹1).
# Input
# * Lily’s age (N)
# * Nothing else (price of toys is not needed because we are not selling)
# Output
# * Number of toys
# * Total money (formatted with 2 decimal places)