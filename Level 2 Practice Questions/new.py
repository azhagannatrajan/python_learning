# write a function to print all numbers from  a to b using loop
# a = start and b = end

# a = int(input("Enter your start number: "))
# b = int(input("Enter your end number: "))

# while a <= b :
#     print(a)
#     a += 1

# write a function to count how many numbers are divisible by a given number between a and b
# a = start , b = end and n = divisor of the numbers between a and b

# a = int(input("Enter 1st: "))
# b = int(input("Enter 2nd: "))
# n = int(input("Enter Divisor number: "))

# def count_num(a,b,n) :
#     count = 0
#     for i in range (a,b+1) :
#         if i%n == 0 :
#             count += 1
#             print(i)
#         i += 1
#     print("Count =",count)
# count_num(2,10,4)

# For a smart watch, you need to write a function to calculate total start points for a given walking steps
# For every 1000 steps = 5 points
# Every 5000th step = 2 bonus points

# def star_points(n) :
#     for_1000 = n // 1000 * 5
#     for_5000 = n // 5000 * 20
#     total_points = for_1000+for_5000
#     print("Total star points =",total_points)
# star_points(20000)

# Question 4

# c_num = int(input("enter your coach number: "))

# if c_num > 10 :
#     print("Invalid coach number")
# elif c_num%2 != 0 :
#     print("Sleeper")
# elif  c_num %2 == 0:
#     print("AC")

# question 5

# n = int(input("enter your coach number: "))
# count = 0 
# while n > 0 :
#     n //= 10
#     count += 1
# print(count)

# question 6

