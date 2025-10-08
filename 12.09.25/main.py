# # x = 5
# # y = 3


# # print(x>y) #greater 
# # print(x<y) #lesser
# # print(x==y) #equal
# # print(x<=y) #lesser or equal
# # print(x>=y) #greater or equal
# # print(x!=y) #not equal



# # #Step 1 - Get input from the user
# # n = int(input("Enter your Number = "))
# # print("You have entered n = ", n)

# # # Step 2 - write condition  
# # if n%2==0:
# #      print("the number is even ",)
# # else :
# #     print("the number is odd ",)



# # #asking the input number
# # N = int(input("Enter the number "))
# # print(N)

# # #writing the condition
# # if N/3==0 or N/5==0:
# #     print("Divisible")
# # else : 
# #     print("Not Divisible")

# # #getting the input
# A = int(input("Enter Your Year "))

# #writing the condition
# if A >= 2001 and A <= 2100:
#     print("21st century")
# else:
#     print("Not in 21st century")
# X = int(input("Enter your mark "))
# print(X)
# if 80 <= X <= 100:
#     print("A")
# elif 60 <= X <= 79:
#     print("B")
# elif 50 <= X <= 59:
#     print("C")
# elif  40 <= X <= 49:
#     print("D")
# else :
#     print("Fail")







# # To check if they can form a triangle
# a = int(input("Enter the first number = "))
# b = int(input("Enter the second number = "))
# c = int(input("Enter the third number = "))
# if a + b > c :
#     print("YES")
# else :
#     print("NO")



# # To find age
# a = int(input("Enter your age in positive integer "))
# print(a)
# if a < 13 :
#     print("Child")
# elif 13<= a <= 19 :
#     print("Teen")
# elif 20<= a <= 59 :
#     print("Adult")
# elif 60<= a <=100 :
#     print("Senior")
# else :
#     print("Invalid age")


amount = int(input("Enter your amount "))

if amount >= 1000 :
    for_1000 = (amount*0.10)
    print(amount - for_1000)

elif amount >= 500 and amount <= 1000:
    for_500_1000 = (amount*0.05)
    print("Your Final price is " , amount - for_500_1000)

else :
    print("No discount for ",amount)