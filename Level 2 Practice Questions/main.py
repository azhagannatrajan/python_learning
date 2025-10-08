# Question 1:
# A cinema charges:
# * ₹150 for ages under 18
# * ₹250 for ages 18–60
# * ₹100 for ages above 60
# Write a program that asks for age and prints the ticket price.
# Sample Input:
# 65
# Sample Output:
# 100



# age = int(input("Enter your age: "))

# if age < 18 : 
#     print("₹150")
# elif age >= 18 and age <=60 :
#     print("₹250")
# elif age > 60 :
#     print("₹100")
# elif age < 0 :
#     print("Invalid Input")



# Question 2:
# A stadium sells entry passes with the following rules:
# * If age < 12 → Ticket = ₹50
# * If age between 12–59 → Ticket = ₹120
# * If age ≥ 60 → Ticket = ₹80
# Additionally, if the person’s age is a Even number, give a ₹5 discount.
# Get the input from the user and return the final discounted stadium ticket price.
# Sample Input:
# 59
# Sample Output:
# 120

# age = int(input("Enter your age: "))

# if age < 12 :
#     price = 50
# elif age <= 59 :
#     price = 50
# elif age >= 60 :
#     price = 50

# if age % 2 == 0 :
#     price -= 5
# print(price)


# Question 3:
# A shopkeeper has n mangoes.
# He wants to pack them into baskets, with 5 mangoes in each basket.
# Write a program to calculate:
# * How many full baskets can be made
# * How many mangoes will be left
# Sample Input:
# 23
# Sample Output:
# Full Basket is 4
# Left Over mangoes is 3

# n = int(input("Enter number of mangoes: "))

# full = n // 5
# left = n % 5

# print("Full Basket = ",full)
# print("Left over = ",left)


# Question 4:
# A child has n candies and eats one candy each day until all are finished.
# Write Python program to print how many candies the child ate and how many are left each day.
# Sample Input:
# 3
# Sample Output:
# Day 1 = 2 left
# Day 2 = 1 left
# Day 3 = 0 left

# n = int(input("Enter number of candies: "))

# for i in range(1, n+1) :
#     left = n - i
#     print(f"day {i} = {left} left")

# Question 5:
# An employee gets a monthly salary.
# * If sales ≥ 100 units → bonus = 10%
# * 50–99 units → bonus = 5%
# * <50 → no bonus
# Write a program that asks for salary and sales and prints total salary including bonus.
# Sample Input:
# Enter your salary 40000
# Enter your sales 120
# Sample Output:
# Bonus = 4000
# Total Salary = 44000

# salary = int(input("Enter your Salary: "))
# sales = int(input("Enter your sales: "))

# if sales >= 100 :
#     bonus = 0.10
# elif sales <=99 : 
#     bonus = 0.05
# elif sales < 50 :
#     print("no Bonus")

# bonus_amt = bonus*salary
# print("Bonus = ",int(bonus_amt))
# total = bonus_amt+salary
# print("Total amount = ",int(total))


# Question 6:
# Earnings of a Salesperson:
# * 5% commission for sales ≤ ₹5000
# * 10% for sales 5001–10000
# * 15% for sales > 10000
# Input weekly sales of the salesperson and calculate commission.
# Test Cases with their output:
# 7000 -> 700
# 12000 -> 1800
# 11000 -> 1650

# sales = int(input("Enter your sales = "))

# if sales <= 5000 :
#     commission = 0.05
# elif sales <= 10000 :
#     commission = 0.10
# elif sales > 10000 :
#     commission = 0.15

# total = commission*sales
# print(total)

# Question 7:
# Multi-Item Shopping Discount
# * Price > 100 → 10% discount
# * Price 50–100 → 5% discount
# * Price <50 → no discount
# Print discounted price per item
# Test cases with their output:
# 200 → 180
# 80 → 76
# 40 → 40
# 150 → 135

# price = int(input("Enter your price = "))

# if price > 100 :
#     discount = 0.10
# elif price <= 100 :
#     discount = 0.05 
# elif price < 50 :
#     print("No discount")

# cal = discount*price
# total = price - cal

# print(total)


# Question 8:
# A file manager needs to classify files based on their extension.
# .csv  → print output as "This is an Excel File"
# .jpg  → print output as "This is a JPEG File"
# .doc  → print output as "This is a Word File"
# .pdf → print output as "This is a PDF File"
# .py → print output as "This is a Python File"
# .Any other input, print output as "Unknown File Type"
# Print the result based on the input
# Sample Input:
# .csv
# Sample Output:
# This is an Excel file
# Sample input:
# .py
# Sample Output:
# This is a Python File

# file = input("Enter file extension: ")
# if file == ".csv":
#     print("This is an Excel File")
# elif file == ".jpg":
#     print("This is a JPEG File")
# elif file == ".doc":
#     print("This is a Word File")
# elif file == ".pdf":
#     print("This is a PDF File")
# elif file == ".py":
#     print("This is a Python File")
# else:
#     print("Unknown File Type")


# Nine

# km = int(input("Enter distance (km): "))
# if km <= 10:
#     fare = km * 15
# elif km <= 30:
#     fare = (10 * 15) + (km - 10) * 12
# else:
#     fare = (10 * 15) + (20 * 12) + (km - 30) * 10
# print(fare)


# Ten


n = int(input("Enter Lily's age: "))
toy = 0 
money = 0 
sum = 0 
for i in range (1,n+1) :
    if i % 2 != 0 :
        toy += 1
    else : 
        sum += 10
        money += sum
print(toy)
print(f"{money:.2f}")








